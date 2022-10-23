from mongoengine import Document, StringField, IntField

class User(Document):
    name = StringField(required=True)
    age = IntField(required=True)

user = User(name='John')
user.validate()

user.errors
# {'age': ['Field is required']}