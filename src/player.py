# Write a class to hold player information, e.g. what room they are in
# currently.
from typing import List

class Player:
    def __init__(self, name: str, current_room, items: List[str] = []):
        self.name = name
        self.current_room = current_room 
        self.items = items
    def __str__(self) -> str:
        return "{self.name} is in the {self.current_room.name} \n{self.current_room.description}".format(self=self)

    def show_inventory(self)-> str:
        # if the player has any items
        if len(self.items) >= 1:
            # number the items
            i = 1
            options = ""
            for item in self.items:
                # itemized list of items in player inventory
                options += F"{str(i)}. {item} "
                # number for next item
                i += 1
            return F"Here are the items in {self.name}'s inventory: {options}\nType n for none."
        else: return ""

    def get_item(self, item_choice: str) -> str:
        # convert the number chosen into an int
        # reduce the number down to an index of the list
        item_choice = int(item_choice) - 1
        # pop out the item in the room at specified index
        item_choice = self.current_room.items.pop(item_choice)
        # player picks up item
        self.items.append(item_choice)
        return F"{self.name} now has a {item_choice}"
    
    def drop_item(self, item_choice: str) -> str:
        # convert the number chosen into an int
        # reduce the number down to an index of the list
        item_choice = int(item_choice) - 1
        # assign the value at the index of items
        # or rather grab that item
        item_choice = self.items.pop(item_choice)
        # drop item in the room
        # room now has the most recently dropped item
        self.current_room.items.append(item_choice)
        return F"{self.name} dropped a {item_choice} in the {self.current_room.name}"
