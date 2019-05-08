import mongoengine

# EmpDetails
class EmpDetails(mongoengine.Document):
    emp_id = mongoengine.IntField(unique=True)
    first_name = mongoengine.StringField()
    last_name = mongoengine.StringField()
    dining_hall = mongoengine.StringField()
    slot_hours = mongoengine.DictField()
    no_of_hours = mongoengine.FloatField(max_value=20.0)

# class CoverPool
#class CoverPool(mongoengine.Document):

