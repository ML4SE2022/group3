from google.appengine.ext import db

class Person(db.Model):
    name = db.StringProperty()

class Car(db.Model):
    owner = db.ReferenceProperty(Person)

query = Car.all()
query.filter('owner =', Person.get_by_key_name('John'))