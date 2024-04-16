from datetime import datetime


class Note:
    def __init__(self, note_id, title, message, timestamp=None):
        self.note_id = note_id
        self.title = title
        self.message = message
        self.timestamp = timestamp or datetime.now().isoformat()