from operator import attrgetter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return repr((self.name, self.age))

people = [Person('John', 30), Person('Adam', 20), Person('Smith', 40)]

print(sorted(people, key=attrgetter('age')))