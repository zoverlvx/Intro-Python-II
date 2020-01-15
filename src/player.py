# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room 
    def states_location(self):
        print(F"{self.name} is in the {self.current_room.name} which is {self.current_room.description}")
