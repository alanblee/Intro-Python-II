from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south....but the smell of rot creeps into your nose from the west...""",
    ),
    "stench": Room(
        "Graveyard of Bones",
        """You enter a cavern with a giant pit filled with rotting flesh and bones. Could this be a lair of a dragon? Possibly filled with
        treasure or sneak out before whatever is living here finds you.""",
    ),
}


# Link rooms together
# change W
room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]
room["treasure"].w_to = room["stench"]
room["stench"].e_to = room["treasure"]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_input = input("Hello adventurer, please tell me your name \n")
new_player = Player(new_input, room["outside"])

# Write a loop that:
# welcome the user and let them know where they are
# print(
#     f"Welcome {new_player.name}, you are currently {new_player.current_room.name}, {new_player.current_room.description}"
# )

# change room function
def change_room():
    new_player.move(selection[0])
    if getattr(new_player.current_room, f"{selection}_to") is None:
        print(
            "========================================\nThat's a dead end, you can't move that way \n========================================"
        )


while True:
    selection = input(
        (
            f"\n ---------------------- \n {new_player} \n ---------------------- \n Press [N] for NORTH \n Press [S] for SOUTH \n Press [W] for WEST \n Press [E] for EAST \n Press [Q] to quit \n"
        )
    ).split(" ")

    if selection[0] == "q":
        print("See you next time")
        break
    # elif new_player.current_room.name == "Treasure Chamber":
    #     print("You left the cave empty handed. Try again in version 2")
    #     break
    try:
        if selection[0] == "n" or "s" or "w" or "e":
            change_room()
    except AttributeError:
        print("Invalid option, please try again")

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
