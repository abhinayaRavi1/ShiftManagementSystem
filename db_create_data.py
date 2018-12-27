import db_schema
import mongoengine
mongoengine.connection.connect('employee', host='localhost', port=27017)

#obj1 = db_schema.EmpDetails(emp_id=10, first_name="Second", last_name="Emp", dining_hall= "App", slot_hours=["4:45pm-9pm"],no_of_hours=4.5).save()