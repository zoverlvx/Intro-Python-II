from room import Room
from player import Player


# Receives player's name
player_name = input("What's your name?: ")

# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     []
                     ),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["torch", "rock"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["rock", "rock", "sparkly rock"]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["dead rat", "...is that lettuce?", "mushroom"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["empty treasure chest"]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(player_name, room["outside"])

"""
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
"""

while True:
    # prints __str__ of player
    print(player)
    # shows quantity of items in current room
    print(player.current_room.show_items())

    # if player has items in their inventory
    if len(player.items) >= 1:
        print(player.show_inventory())
        choice=input("Drop this item: ")
        if choice is not "n":
            print(player.drop_item(choice))
        elif choice is "n":
            print(F"{player.name} continues on.")

    # if there are items in the room
    if len(player.current_room.items) >= 1:
        # displays item choices
        print(player.current_room.display_item_choices())
        choice=input("Make your choice: ")
        if choice is not "n":
            print(player.get_item(choice))
        elif choice is "n":
            print("No items picked up.")
    
    possible_directions = ["n", "s", "w", "e"]

    direction=input("Which direction would you like to go? (N, S, W, E, or Q for quit): ").lower()

    if direction == "q":
        print("Thanks for playing")
        break
    
    # if direction is possible
    if direction in possible_directions:
        # if the room has an adjoining room of that direction
        if hasattr(player.current_room, F"{direction}_to"):
            # player moves to room indicated by direction taken
            player.current_room = getattr(player.current_room, F"{direction}_to")
        else:
            print("There doesn't appear to be a room there. Try again, please.\n")
    else:
        print("Incorrect direction. Please, try again.\n")
