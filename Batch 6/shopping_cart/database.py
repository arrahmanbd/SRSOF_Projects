import sqlite3
db = sqlite3.connect("shopping_cart.db")

# Creating table
def createTable():
    db.execute(
        """
    CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
        )
        """
    )

# Adding item to cart
def addItem():
    print("Add item to cart:")
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    db.execute(
        '''
        INSERT INTO items(name, price)
        VALUES(?, ?)
        ''',
        (name, price,)
    )
    db.commit()
    showItems()

# Showing items in cart
def showItems():
    data = db.execute(
        '''
        SELECT * FROM items
        '''
    )
    item_list = data.fetchall()
    print("Items in the cart:")
    print('-' * 20)
    for item in item_list:
        print(f"{item[0]}. {item[1]} :{item[2]}")
    calculateTotal(item_list)

# Calculate total cost of items
def calculateTotal(item_list):
    total_cost = sum(item[2] for item in item_list)
    print('-' * 20)
    print(f"You have to Pay: {total_cost}")

# Delete item from cart
def deleteItem():
    item_id = int(input('Enter item ID to delete: '))
    db.execute(
        '''
        DELETE FROM items WHERE id=?
        ''',
        (item_id,)
    )
    db.commit()
    showItems()

# Update item in cart
def updateItem():
    print("Update item:")
    item_id = int(input("Enter item ID to update: "))
    new_name = input("Enter new item name: ")
    new_price = float(input("Enter new item price: "))
    db.execute(
        '''
        UPDATE items SET name=?, price=? WHERE id=?
        ''',
        (new_name, new_price, item_id,)
    )
    db.commit()
    showItems()


