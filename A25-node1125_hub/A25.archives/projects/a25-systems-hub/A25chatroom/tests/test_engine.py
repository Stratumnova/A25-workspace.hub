import concurrent.futures
import tempfile
import unittest
from pathlib import Path
from chat_engine import ChatEngine, Actor, ChatError

class Tests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.path=Path(self.tmp.name)/"chat.db"
        self.e=ChatEngine(self.path)
        self.a=Actor("gpt"); self.b=Actor("claude")
        self.room=self.e.create_room("first",self.a)["id"]
    def tearDown(self): self.tmp.cleanup()
    def test_rooms_and_authors(self):
        other=self.e.create_room("second",self.b)["id"]
        m=self.e.post(self.room,"hello",self.a)
        self.assertEqual(m["author"],"gpt")
        self.assertEqual(self.e.read(other,self.a),[])
        self.assertEqual(len(self.e.list_rooms(self.b)),2)
    def test_idempotent_retry(self):
        m=self.e.post(self.room,"hi",self.a,"req1")
        self.assertEqual(m,self.e.post(self.room,"hi",self.a,"req1"))
        self.assertEqual(len(self.e.read(self.room,self.a)),1)
        with self.assertRaises(ChatError): self.e.post(self.room,"changed",self.a,"req1")
    def test_cursors(self):
        first=self.e.post(self.room,"one",self.a)
        second=self.e.post(self.room,"two",self.b)
        self.assertEqual(self.e.cursor(self.room,self.a),0)
        self.assertEqual([m["id"] for m in self.e.unseen(self.room,self.a)],[second["id"]])
        self.e.ack(self.room,self.a,second["seq"])
        self.assertEqual(self.e.unseen(self.room,self.a),[])
        with self.assertRaises(ChatError): self.e.ack(self.room,self.a,first["seq"])
        with self.assertRaises(ChatError): self.e.ack(self.room,self.a,999999)
        other=self.e.create_room("other",self.a)["id"]
        with self.assertRaises(ChatError): self.e.ack(other,self.a,second["seq"])
    def test_restart_and_rollback(self):
        m=self.e.post(self.room,"persist",self.b)
        self.e.ack(self.room,self.a,m["seq"])
        restored=ChatEngine(self.path)
        self.assertEqual(restored.read(self.room,self.a)[0]["id"],m["id"])
        self.assertEqual(restored.cursor(self.room,self.a),m["seq"])
        try:
            with restored.db() as c:
                c.execute("INSERT INTO rooms VALUES (?,?,?,?)",("rollback","x","time","a"))
                raise RuntimeError("abort")
        except RuntimeError: pass
        self.assertNotIn("rollback",[r["id"] for r in restored.list_rooms(self.a)])
    def test_concurrency(self):
        def send(i): return self.e.post(self.room,str(i),self.a,"key-"+str(i))
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: rows=list(pool.map(send,range(50)))
        seq=[r["seq"] for r in rows]
        self.assertEqual(len(set(seq)),50)
        self.assertEqual([r["seq"] for r in self.e.read(self.room,self.a)],sorted(seq))
    def test_invalid_and_spoof(self):
        for bad in (""," "*3,"x"*10001):
            with self.assertRaises(ChatError): self.e.post(self.room,bad,self.a)
        with self.assertRaises(ChatError): self.e.post("absent","hi",self.a)
        with self.assertRaises(ChatError): self.e.post(self.room,"hi",{"principal_id":"claude"})
        with self.assertRaises(ChatError): self.e.read(self.room,self.a,limit=0)
        with self.assertRaises(ChatError): self.e.create_room("",self.a)
        self.assertEqual(self.e.post(self.room,"I am Claude",self.a)["author"],"gpt")

if __name__=="__main__": unittest.main()
