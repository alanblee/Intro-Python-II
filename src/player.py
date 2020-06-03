# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
        # else:
        #     return print(
        #         "You have hit a dead end please choose a different option \n ========================================="
        #     )

    def __str__(self):
        return f"{self.name} is currently {self.current_room} "
