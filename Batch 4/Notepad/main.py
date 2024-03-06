from database import*
create_table()
#Menu for add,update,delete notes
while True:
    print('\nWelcome To Notepad','-'*5, '😃')
    print("1. Add Note\n2. Update Note\n3. Read Notes\n4. Delete Note\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        note_title = input("Enter note title: ")
        note = input("Enter note: ")
        create_note(note_title, note)
    elif choice == '2':
        note_number = int(input("Enter note number to update: "))
        new_note_title = input("Enter new note title: ")
        new_note = input("Enter new note: ")
        update_note(note_number, new_note_title, new_note)
    elif choice == '3':
        get_all_notes()
    elif choice == '4':
        note_number = int(input("Enter note number to delete: "))
        delete_note(note_number)
    elif choice == '5':
        print("Exiting Notepad. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
