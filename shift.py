import pymongo
from pprint import pprint

TEST_DATA = [
    {
        'emp_id': 123456,
        'first_name': 'Tom',
        'last_name': 'Jonas',
        'dining_hall': 'CIW',
        'slot_hours': {"Mon": "4:45pm-9pm"},
        'no_of_hours': 4.5
    },
    {
        'emp_id': 678901,
        'first_name': 'Adam',
        'last_name': 'Green',
        'dining_hall': 'Hinman',
        'slot_hours': {"Tue": "6pm-9pm"},
        'no_of_hours': 3
    },
    {
        'emp_id': 246810,
        'first_name': 'John',
        'last_name': 'Berg',
        'dining_hall': 'Hinman',
        'slot_hours': {"Wed": "10am-2pm", "Thur": "6pm-9pm"},
        'no_of_hours': 7
    }
]


# Employee details
def display_emp_details(emp_db):
    print("Employee Details:")
    cursor = emp_db.find()
    for doc in cursor:
        pprint(doc)


# Give cover
def give_cover(db):
    emp_id, slot_time = input("Enter employee id and slot to give").split()
    db.coverPool.insert_one({'emp_id': emp_id, 'slot_time': slot_time})
    print("Tested")

# Take cover
def take_cover(db):

    print("Displaying the Cover Pool table")
    cover_db = db['coverPool']
    cur1 = cover_db.find()
    for dc in cur1:
        pprint(dc)

    ''' 
        If a person can take cover, then the following conditions are to be met:
            1. If the shift clashes with his own
            2. If the number of work hours is greater than 20
    '''
    emp_db = db['empDetails']
    emp_id_in = int(input("Enter your employee ID"))
    '''
    Query empDetails 
    '''
    res = []
    my_doc = emp_db.find({'emp_id': emp_id_in}, {'no_of_hours': 1})
    for doc in my_doc:
        res.append(doc)
    print(res)

# Driver function
def main():


    uri = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(uri)
    db = client["employee"]
    emp_db = db["empDetails"]

    emp_db.insert_many(TEST_DATA)
    
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
            display_emp_details(emp_db)
        elif choice == 2:
            give_cover(db)
        elif choice == 3:
            take_cover(db)
        elif choice == 4:
            print("Adios!")
            # exit(0)
        else:
            print("Enter valid option")

    db.empDetails.delete({})
    client.close()


if __name__ == '__main__':
    main()

