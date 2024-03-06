from act import*
from db import*

def main():
    conn = create_connection('students_marks.db')
    create_table(conn)

    while True:
        print('\n1. Add Student Info\n2. Read All Student Info\n3. Update Student Info\n4. Delete Student Info\n5. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            roll = int(input('Enter Student Roll: '))
            name = input('Enter Student Name: ')
            marks = int(input('Enter Student Mark:'))
            create_student(conn, roll, name, marks)

        elif choice == '2':
            get_all_students(conn)

        elif choice == '3':
            roll = input('Enter Student Roll: ')
            name = input('Enter New Student Name: ')
            marks = int(input('Enter Student Marks:'))
            update_name(conn, roll, name, marks)

        elif choice == '4':
            roll = input('Enter student roll to delete: ')
            delete_student(conn, roll, marks)

        elif choice == '5':
            break

        else:
            print('Invalid choice. Please try again.')
    conn.close()
    
main()
