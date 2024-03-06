import sqlite3
db = sqlite3.connect("bucket.db")

# Creating table
def createTable():
    db.execute(
        """
    CREATE TABLE IF NOT EXISTS bucket(
        id INTEGER PRIMARY KEY,
        title TEXT,
        price REAL
        )
        """
    )

# Adding item to the bucket
def addItem():
    print("Add item to bucket:")
    title = input("Enter item title: ")
    price = float(input("Enter item price: "))
    db.execute(
        '''
        INSERT INTO bucket(title, price)
        VALUES(?, ?)
        ''',
        (title, price,)
    )
    db.commit()
    showbucket()

# Showing bucket in the bucket
def showbucket():
    data = db.execute(
        '''
        SELECT * FROM bucket
        '''
    )
    bucket_list = data.fetchall()
    print("bucket in the the bucket:")
    print('-' * 20)
    for item in bucket_list:
        print(f"{item[0]}. {item[1]} :{item[2]}")
    total_cost = sum(item[2] for item in bucket_list)
    print('-' * 20)
    print(f"Total cost: {total_cost}")

# Delete item from the bucket
def deleteItem():
    item_id = int(input('Enter item ID to delete: '))
    db.execute(
        '''
        DELETE FROM bucket WHERE id=?
        ''',
        (item_id,)
    )
    db.commit()
    showbucket()

# Update item in the bucket
def updateItem():
    print("Update item:")
    item_id = int(input("Enter item ID to update: "))
    new_title = input("Enter new item title: ")
    new_price = float(input("Enter new item price: "))
    db.execute(
        '''
        UPDATE bucket SET title=?, price=? WHERE id=?
        ''',
        (new_title, new_price, item_id,)
    )
    db.commit()
    showbucket()


