import mongoengine



# EmpDetails table
class EmpDetails(mongoengine.Document):
    emp_id = mongoengine.IntField(unique=True)
    first_name = mongoengine.StringField()
    last_name = mongoengine.StringField()
    dining_hall = mongoengine.StringField()
    slot_hours = mongoengine.ListField()
    no_of_hours = mongoengine.FloatField()


