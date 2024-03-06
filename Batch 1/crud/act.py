

def create_student(conn, student_roll, name, marks):
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO students (student_roll, name, marks) VALUES (?,?,?)", (student_roll, name, marks))
        conn.commit()
        print(f'Student with roll {student_roll} . name: {name} and marks: {marks} created successfully ')
        get_all_students(conn)
    except conn.IntegrityError:
       
        print(f'Error: Student with roll {student_roll} already exists in the database.')


def get_all_students(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    print('\nAll Info:')
    for student in students:
        print(f'Roll: {student[0]}, Name: {student[1]}, marks: {student[2]}')

def update_name(conn, student_roll, new_name, new_marks):
    cursor = conn.cursor()
    cursor.execute('UPDATE students SET name = ? WHERE roll = ?', (new_name, student_roll, new_marks))
    conn.commit()
    print(f'Student with roll {student_roll} updated. New name: {new_name}. New marks {new_marks}')

def delete_student(conn, student_roll):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE roll = ?', (student_roll,))
    conn.commit()
    print(f'Student with roll {student_roll} deleted successfully.')
