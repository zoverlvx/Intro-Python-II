# Implement a class to hold room information. This should have name and
# description attributes.
from typing import List

class Room:
    def __init__(self, name: str, description: str, items: List[str]):
        self.name = name
        self.description = description
        self.items = items
    def show_items(self):
        return F"{self.name} has {len(self.items)} items in it."
