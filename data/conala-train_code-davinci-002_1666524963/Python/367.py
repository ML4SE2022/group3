class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '{} is {} years old'.format(self.name, self.age)


people = [
    Person('Alice', 25),
    Person('Bob', 30),
    Person('Charlie', 50),
    Person('Dan', 21)
]

# sort by age
people.sort(key=lambda person: person.age)
print(people)

# sort by name
people.sort(key=lambda person: person.name)
print(people)