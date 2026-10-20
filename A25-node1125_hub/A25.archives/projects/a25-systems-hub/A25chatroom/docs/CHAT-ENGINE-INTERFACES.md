# Chat engine Stage 1 interface

Local Python library only. Requires Python 3.10+ and standard library SQLite.

Run from A25chatroom root: `python -m unittest discover -s tests -v`.

`ChatEngine(path)` initializes SQLite schema at the given local path. Call `create_room(name, Actor)`, `list_rooms(Actor)`, `post(room_id,text,Actor,request_id=None)`, `read(room_id,Actor,after_seq=0,limit=100)`, `cursor(room_id,Actor)`, `ack(room_id,Actor,seq)`, `unseen(room_id,Actor,limit=100)`.

Rooms and messages have opaque UUIDs. Message seq is SQLite-assigned globally increasing order; UTC timestamps are timezone-aware strings. Posting is append-only and transactional. Client request IDs are unique per principal and reject conflicting retries. Reads never acknowledge. Cursors are per room and principal, monotonic, and can only point to messages in that room. Own messages are excluded from unseen results.

**Security boundary:** Actor is a caller-supplied testing seam, not verified authentication. Production adapters must establish the principal independently of payloads, require permission checks and Security review. Do not expose this library to untrusted callers or a network. No delete, clear, ZIP, API listener, phone integration, or external connector is implemented.

**Known limitation:** `unseen` filters own messages after pagination, so a page containing only own messages may be empty even if later external messages exist. The later adapter must paginate onward rather than treat an empty filtered page as proof that all unread messages have been consumed. No multi-process/network integration tested.
