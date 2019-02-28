import mongoengine

#mongoengine.connection.connect('employee', host='localhost', port=27017)

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


#obj1 = db_schema.EmpDetails(emp_id=10, first_name="Second", last_name="Emp", dining_hall= "Hinman", slot_hours=["4:45pm-9pm"],no_of_hours=4.5).save()
#obj2 = db_schema.EmpDetails(emp_id=10, first_name="Second", last_name="Emp", dining_hall= "Hinman", slot_hours=["4:45pm-9pm"],no_of_hours=4.5).save()



# list_ids = []
# def rand_num():
#     return random.randint(100000, 999999)
#
#
# firstName = ['John', 'Alpha', 'Beta', 'Gamma']
# lastName = ['Gates', 'Jobs', 'Express']
# diningHall = ['Hinman', 'App', 'CIW']
# no_of_hours = [2, 4, 6, 2.5, 20]
# list_ids.append(rand_num())
# print(list_ids)
#
# for x in range(0,5):
#     employee = {
#         'emp_id':
#         'first_name': firstName[random(0,(len(firstName)-1)] ,
#         'last_name':lastName[random(0,len(firstName)-1)] ,
#         'dining_hall':
#     }