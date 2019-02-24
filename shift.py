import db_create_data
import db_schema


# Employee details
def display_emp_details():
    print('Employee Details')
    for user in db_schema.EmpDetails.objects:
        print(str(user.emp_id)+" " + user.first_name+" "+user.last_name+" "+user.dining_hall+" "+" ".join(user.slot_hours)+" " + str(user.no_of_hours))


# Give cover
def give_cover():
    #User id and slot to give - IP
    #Backend - mark that slot
    emp_id, slot_time = input("Enter employee id and slot to give").split()


# Take cover
def take_cover():
    pass

def main():

    db_create_data
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
            display_emp_details()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            print("Enter valid option")


if __name__ == '__main__':
    main()
