import sqlite3
db=sqlite3.connect("phone.db")

#create table
def create_table():
    db.execute(
    '''
    CREATE TABLE IF NOT EXISTS phone_book(
    id INTEGER PRIMARY KEY,
    name TEXT,
    mobile_number INTEGER
    )
    '''
    )
    print("Let's use this phone book Welcome 💗")

#add people
def add_people():
    name=str(input("Enter name:"))
    mobile_number=int(input("Enter mobile number:"))
    db.execute(
    '''
    INSERT INTO phone_book(name,mobile_number)
    VALUES(?,?)
    ''',
    (name,mobile_number)
    )
    db.commit()
    print(f"{name} with mobile number {mobile_number} added")
    print("List has been showed successfully")
    show_phone_book()
def show_phone_book():
    info=db.execute(
    '''
    SELECT * FROM phone_book
    '''
    )
    print("="*20)
    for i in info:
        print(f"id: {i[0]}  name: {i[1]}  mobile_number:  {i[2]}")
    
#updatting info
def update_phoneBook():
    print("Update information")
    mobile_number=int(input("Enter new mobile_number:"))
    user_id=int(input("Enter new user id:"))
    db.execute(
    '''
    UPDATE phone_book SET mobile_number=? WHERE id=?
    ''',
    (mobile_number,user_id)
    )
    db.commit()
    print("Mobile number updatted successfully")
    show_phone_book()

#deleting info
def delete_user_id():
    user_id=int(input("Enter user id to delete:"))
    db.execute(
    '''
    DELETE FROM phone_book WHERE id=?
    ''',
    (user_id,)
    )
    db.commit()
    print("Deleted Successfully")
    show_phone_book()
