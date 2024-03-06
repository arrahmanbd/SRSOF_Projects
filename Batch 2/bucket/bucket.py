from db import*
print("\n🛒 Bucket")
print("*" * 20)
createTable()
while True:
        print("\nBucket Menu:")
        print("1. Add to Bucket")
        print("2. Show Bucket List")
        print("3. Remove from Bucket")
        print("4. Update Bucket")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            addItem()
        elif choice == "2":
            showbucket()
        elif choice == "3":
            deleteItem()
        elif choice == "4":
            updateItem()
        elif choice == "5":
            print("Closing Your Bucket, Thanks for using")
            break
        else:
            print("Invalid Option!")

