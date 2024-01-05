# Public- variable-dont mention anything
# Protected
# Private
# variable & functions

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        return self.__name

    def print_details(self):
        print("Your details", self.__name, self.__age)


person = Person("Basha", 39)
person.print_details()
# print(person.__name)#Private?
# How to change it Get and Set?
# Fetch -Get
# Set The value - constuctor
person.set_name("Basha")
name = person.get_name()
print(name)
person.print_details()
