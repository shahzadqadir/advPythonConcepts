import sys

from notebook import Note, Notebook



class Menu:
    """Display a menu for Notebook app."""
    def __init__(self):
        """initialize a new notebook object"""
        self.note_book = Notebook()

    def menu(self):
        """display a menu for user to chose action to perform"""
        print(
            """
        1. Add a new note
        2. Search a note
        3. Modify a note
        4. Show all notes
        5. Quits
            """
        )
    
    def run(self):
        self.menu()

if __name__ == "__main__":
    menu = Menu()
    menu.run()
    memo_tags = ""
    choice = int(input("Please enter your choice: "))
    if choice >= 5:
        sys.exit(0)
    if choice == 1:
        memo_text = input("Memo text: ")
        memo_tags = input("Tags (can be left empty!): ")
        nb = menu.note_book.add_new_note(memo_text, memo_tags)
    if choice == 2:
        pass
    if choice == 3:
        pass
    if choice == 4:
        print(menu.note_book.notes)
        