"""Local-only SQLite chat. Actor is trusted injection seam, NOT production authentication."""
from dataclasses import dataclass
from datetime import datetime, timezone
from contextlib import contextmanager
import sqlite3
import uuid

class ChatError(ValueError): pass

@dataclass(frozen=True)
class Actor:
    principal_id: str
    role: str = "test"

def utc(): return datetime.now(timezone.utc).isoformat()

def principal(actor):
    if not isinstance(actor,Actor) or not isinstance(actor.principal_id,str) or not actor.principal_id.strip():
        raise ChatError("trusted actor required")
    return actor.principal_id

SCHEMA = """
CREATE TABLE IF NOT EXISTS rooms(id TEXT PRIMARY KEY,name TEXT NOT NULL,created_at TEXT NOT NULL,creator TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS messages(seq INTEGER PRIMARY KEY AUTOINCREMENT,id TEXT UNIQUE NOT NULL,room_id TEXT NOT NULL REFERENCES rooms(id),author TEXT NOT NULL,created_at TEXT NOT NULL,text TEXT NOT NULL,request_id TEXT,UNIQUE(author,request_id));
CREATE INDEX IF NOT EXISTS room_seq ON messages(room_id,seq);
CREATE TABLE IF NOT EXISTS cursors(room_id TEXT NOT NULL REFERENCES rooms(id),reader TEXT NOT NULL,through_seq INTEGER NOT NULL,updated_at TEXT NOT NULL,PRIMARY KEY(room_id,reader));
"""

class ChatEngine:
    def __init__(self,path):
        self.path=str(path)
        with self.db() as c: c.executescript(SCHEMA)
    @contextmanager
    def db(self):
        c=sqlite3.connect(self.path,timeout=15)
        c.row_factory=sqlite3.Row
        c.execute("PRAGMA foreign_keys=ON")
        c.execute("PRAGMA busy_timeout=15000")
        try:
            yield c
            c.commit()
        except BaseException:
            c.rollback()
            raise
        finally:
            c.close()
    def require_room(self,c,room):
        if not c.execute("SELECT 1 FROM rooms WHERE id=?",(room,)).fetchone(): raise ChatError("unknown room")
    def create_room(self,name,actor):
        who=principal(actor)
        if not isinstance(name,str) or not name.strip() or len(name)>200: raise ChatError("invalid room name")
        row=dict(id=str(uuid.uuid4()),name=name.strip(),created_at=utc(),creator=who)
        with self.db() as c: c.execute("INSERT INTO rooms VALUES (:id,:name,:created_at,:creator)",row)
        return row
    def list_rooms(self,actor):
        principal(actor)
        with self.db() as c: return [dict(r) for r in c.execute("SELECT * FROM rooms ORDER BY created_at,id")]
    def post(self,room,text,actor,request_id=None):
        who=principal(actor)
        if not isinstance(text,str) or not text.strip() or len(text)>10000: raise ChatError("invalid text")
        if request_id is not None and (not isinstance(request_id,str) or not request_id.strip() or len(request_id)>200): raise ChatError("invalid request id")
        with self.db() as c:
            c.execute("BEGIN IMMEDIATE")
            self.require_room(c,room)
            if request_id is not None:
                old=c.execute("SELECT * FROM messages WHERE author=? AND request_id=?",(who,request_id)).fetchone()
                if old:
                    if old["room_id"]!=room or old["text"]!=text: raise ChatError("request id collision")
                    return dict(old)
            row=dict(id=str(uuid.uuid4()),room_id=room,author=who,created_at=utc(),text=text,request_id=request_id)
            row["seq"]=c.execute("INSERT INTO messages(id,room_id,author,created_at,text,request_id) VALUES (:id,:room_id,:author,:created_at,:text,:request_id)",row).lastrowid
            return row
    def read(self,room,actor,after_seq=0,limit=100):
        principal(actor)
        if type(after_seq)!=int or after_seq<0 or type(limit)!=int or not 1<=limit<=500: raise ChatError("invalid pagination")
        with self.db() as c:
            self.require_room(c,room)
            return [dict(r) for r in c.execute("SELECT * FROM messages WHERE room_id=? AND seq>? ORDER BY seq LIMIT ?",(room,after_seq,limit))]
    def cursor(self,room,actor):
        who=principal(actor)
        with self.db() as c:
            self.require_room(c,room)
            r=c.execute("SELECT through_seq FROM cursors WHERE room_id=? AND reader=?",(room,who)).fetchone()
            return r["through_seq"] if r else 0
    def ack(self,room,actor,seq):
        who=principal(actor)
        if type(seq)!=int or seq<0: raise ChatError("invalid cursor")
        with self.db() as c:
            c.execute("BEGIN IMMEDIATE")
            self.require_room(c,room)
            r=c.execute("SELECT through_seq FROM cursors WHERE room_id=? AND reader=?",(room,who)).fetchone()
            if r and seq<r["through_seq"]: raise ChatError("backward cursor")
            if seq and not c.execute("SELECT 1 FROM messages WHERE room_id=? AND seq=?",(room,seq)).fetchone(): raise ChatError("foreign or absent cursor")
            c.execute("INSERT INTO cursors VALUES (?,?,?,?) ON CONFLICT(room_id,reader) DO UPDATE SET through_seq=excluded.through_seq,updated_at=excluded.updated_at",(room,who,seq,utc()))
            return seq
    def unseen(self,room,actor,limit=100):
        who=principal(actor)
        if type(limit)!=int or not 1<=limit<=500: raise ChatError("invalid pagination")
        with self.db() as c:
            self.require_room(c,room)
            cursor=c.execute("SELECT through_seq FROM cursors WHERE room_id=? AND reader=?",(room,who)).fetchone()
            through=cursor["through_seq"] if cursor else 0
            return [dict(m) for m in c.execute(
                "SELECT * FROM messages WHERE room_id=? AND seq>? AND author<>? ORDER BY seq LIMIT ?",
                (room,through,who,limit))]
