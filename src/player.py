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

    def get_item(self, item_choice: str) -> str:
        item_choice = int(item_choice) - 1
        self.items.append(self.current_room.items.pop(item_choice))
        return F"{self.name} now has a {self.items[item_choice]}"

