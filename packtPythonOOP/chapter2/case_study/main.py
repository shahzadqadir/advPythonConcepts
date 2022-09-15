from notebook import Note, Notebook

nb1 = Notebook()
nb1.add_new_note("my first note, again", "first first first")
nb1.add_new_note("my second note, again", "second second second")

nb1.modify_memo(2, "my second updated note.")

nb1.modify_memo(1, "note1, let me update you again, hope you don't mind.")
print(nb1._search_note(1))