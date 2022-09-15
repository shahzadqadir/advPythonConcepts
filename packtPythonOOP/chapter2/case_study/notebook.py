import datetime

class Note:
    last_id = 0
    """Represent a note in the notebook. Match against a string in searches and store tags for each note.
    """
    def __init__(self, memo, tags=""):
        """initialize a note with memo and stores tags for each note. tags are space spearated
        automatically set note creation date and note id.
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        Note.last_id += 1
        self.id = Note.last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags

    def __str__(self):
        return self.memo


class Notebook:
    """contains Note class objects
    """
    def __init__(self):
        """initialize a notebook object with empty note objects list"""
        self.notes = []

    def add_new_note(self, memo, tags=""):
        """Add a note object to the list of objects
        """
        self.notes.append(Note(memo, tags))

    def _search_note(self, note_id):
        """Search a note from list of note objects using note_id"""
        if note_id <= len(self.notes):
            for note in self.notes:
                if note.id == note_id:
                    return note
        return None


    def modify_memo(self, note_id, new_memo):
        """Search a note using note id and then update it's memo description"""
        if self._search_note(note_id):
            self._search_note(note_id).memo = new_memo

    def modify_tags(self, note_id, new_tags):
        """Search a notes using note id and replace tag string with new one"""
        if self._search_note(note_id):
            self._search_note(note_id).tags = new_tags

    def search(self, search_string):
        """Find all notes matching a search string, 
        return a list of notes found.
        """
        [note for note in self.notes if note.match(search_string)]

    def __str__(self):
        return f"Notebook with {len(self.notes)} notes"