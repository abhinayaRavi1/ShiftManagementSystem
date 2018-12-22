import pymongo



# Connect to MongoDB
uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
db = client['employee']

choice = -1
# Menu Based interface
while choice != 4:
    print("Enter option from the below menu")
    print("1.Display employee details")
    print("2.Give cover")
    print("3.Take cover")
    print("4.Exit")
    choice = int(input("Enter choice"))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    else:
        print("Enter valid option")




