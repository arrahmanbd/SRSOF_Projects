import database as db
db.create_table()
while True:
    print("*"*20)
    print(f"1.Add People\n2.Update Name\n3.Delete \n4. Show All \n5.Exit")
    select=int(input("select an option:"))
    if select==1:
        db.add_people()
    if select==2:
        db.update_phoneBook()
    if select==3:
        db.delete_user_id()
    if select==4:
        db.show_phone_book()
    if select==5:
        print("Thanks For Using Our Programme 🤗")
        break