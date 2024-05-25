#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

# Creating instances of Dog
fido = Dog(name="Fido", breed="Dalmatian")
buddy = Dog(name="Buddy")  

# Calling instance methods
fido.bark()
fido.sit()
buddy.bark()
buddy.sit()

