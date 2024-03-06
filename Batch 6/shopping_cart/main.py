from database import*
print("\n🛍️ Let's Shop🛒")
print("*" * 20)
#Connecting to our database
# Main function to manage shopping cart

createTable()
while True:
        print("\nShopping Cart Menu:")
        print("1. Add Item")
        print("2. Show Items")
        print("3. Delete Item")
        print("4. Update Item")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            addItem()
        elif choice == "2":
            showItems()
        elif choice == "3":
            deleteItem()
        elif choice == "4":
            updateItem()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

