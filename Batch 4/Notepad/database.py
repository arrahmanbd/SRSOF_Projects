import sqlite3
conn = sqlite3.connect('note.db')
db = conn.cursor()

def create_table():
    db.execute("CREATE TABLE IF NOT EXISTS note(note_number INTEGER PRIMARY KEY, note_title VARCHAR(50), note TEXT)")

def create_note(note_title, note):
    try:
        db.execute("INSERT INTO note (note_title, note) VALUES (?, ?)", (note_title, note))
        conn.commit()
        print(f'Note : "{note_title}" created successfully')
        get_all_notes()
    except conn.IntegrityError:
        print(f'Error: Note with title "{note_title}" already exists in the database')

def get_all_notes():
    db.execute('SELECT * FROM note')
    notes = db.fetchall()
    print('\n🗒  My notes:')
    print('-'*22)
    for note in notes:
        print(f'[{note[0]}] {'-'*18}\nTitle: {note[1]}\nNote: {note[2]}\n')

def update_note(note_number, new_note_title, new_note):
        db.execute('UPDATE note SET note_title=?, note=? WHERE note_number=?', (new_note_title, new_note, note_number))
        conn.commit()
        print(f'Note: {note_number} updated successfully')
        get_all_notes()

def delete_note(note_number):
    db.execute("DELETE FROM note WHERE note_number=?", (note_number,))
    conn.commit()
    print(f'Note: {note_number} deleted successfully')

