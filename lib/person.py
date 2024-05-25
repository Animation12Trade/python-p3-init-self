#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

# Creating an instance of Person
john = Person(name="John")

# Calling instance methods
john.talk()
john.walk()
