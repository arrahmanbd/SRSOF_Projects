import sqlite3
db = sqlite3.connect("hospital.db")

def create_table():
    db.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            problem TEXT
        )
    ''')

def add_patient():
    name = input("Enter patient's name: ")
    age = int(input("Enter patient's age: "))
    gender = input("Enter patient's gender: ")
    problem = input("Enter patient's problem: ")
    db.execute("INSERT INTO patients (name, age, gender, problem) VALUES (?, ?, ?, ?)",
                (name, age, gender, problem))
    db.commit()


def get_all_patients():
    cursor = db.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    return patients

def update_patient():
    patient_id = int(input("Enter the ID of the patient to update: "))
    name = input("Enter the updated name: ")
    age = int(input("Enter the updated age: "))
    gender = input("Enter the updated gender: ")
    problem = input("Enter the updated problem: ")
    db.execute("UPDATE patients SET name=?, age=?, gender=?, problem=? WHERE id=?",
               (name, age, gender, problem, patient_id))
    db.commit()


def delete_patient():
    patient_id = int(input("Enter the ID of the patient to delete: "))
    db.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    db.commit()


def display_menu():
    print("\nHospital Management System Menu:")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Update Patient")
    print("4. Delete Patient")
    print("5. Exit")


create_table()

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
            add_patient()
    elif choice == "2":
        patients = get_all_patients()
        print("\nPatients:")
        for patient in patients:
            print(patient)
    elif choice == "3":
        update_patient()
    elif choice == "4":
        delete_patient()
    elif choice == "5":
        print("Exiting the Hospital Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

