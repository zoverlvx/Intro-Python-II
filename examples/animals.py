from abc import ABC, abstractmethod
from typing import List

"""
https://www.python-course.eu/python3_abstract_classes.php
https://www.geeksforgeeks.org/abstract-classes-in-python/
https://www.youtube.com/watch?v=aIdzBGzaxUo
"""

class Animal(ABC):
    def __init__(self, name: str, legs: int):
        self.name: str = name
        self.legs: int = legs
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def species(self):
        pass

class Dog(Animal):
    def __init__(self, name: str, legs: int = 4):
        super().__init__(name, legs)
    def speak(self):
        return "Woof!"
    def species(self):
        print("Dog")
    def __str__(self):
        return 'name: {self.name}, legs: {self.legs}'.format(self=self)

class Bird(Animal):
    def __init__(self, name: str, legs: int = 4):
        super().__init__(name, legs)
    def speak(self):
        return "Tweet tweet!"
    def species(self):
        print("Bird")

class Cat(Animal):
    def __init__(self, name: str, legs: int = 4):
        super().__init__(name, legs)
    def speak(self):
        return "Meow"
    def species(self):
        print("Cat")

b = Bird("Larry")
c = Cat("Garfield")
d = Dog("Fido")
print(F"Props of Fido: {d}")

animals = [b, c, d]

for animal in animals:
    print(F"{animal.name} says {animal.speak()}")

class Room:
    def __init__(self, room_type: str):
        self.type: str = room_type
    def __str__(self):
        return self.type
    def __repr__(self):
        return self.type

class Building:
    def __init__(self, name: str, rooms: List[Room]):
        self.name = name
        self.rooms = rooms
    def __str__(self):
        return self.name

bedroom = Room("Bedroom")
bathroom = Room("Bathroom")
house = Building("My house", [bedroom, bathroom])


