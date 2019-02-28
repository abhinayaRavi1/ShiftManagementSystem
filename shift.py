import db_create_data
import db_schema
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
        'first_name':'Adam',
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

# # Employee details
# def display_emp_details():
#     print('Employee Details')
#     for user in db_schema.EmpDetails.objects:
#         print(str(user.emp_id)+" " + user.first_name+" "+user.last_name+" "+user.dining_hall+" "+" ".join(user.slot_hours)+" " + str(user.no_of_hours))

#Employee details
def display_emp_details(emp_db):
    print("Employee Details:")
    cursor = emp_db.find()
    for doc in cursor:
        pprint(doc)

# Give cover
def give_cover():
    #User id and slot to give - IP
    #Backend - mark that slot
    emp_id, slot_time = input("Enter employee id and slot to give").split()
    print(emp_id, slot_time)
    

# Take cover
def take_cover():
    pass

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
            give_cover()
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            print("Enter valid option")


if __name__ == '__main__':
    main()
