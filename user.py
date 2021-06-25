# Jaime Bohorquez
# Programmed using Atom + iTerm2 on Mac OS Big Sur
# Filename: user.py

# Here we define our user class so that we can hold our data.

class GymUser:
    name: str
    email: str
    room: str
    time: str
    def __init__(self, name: str, email: str, time: str, room: str):
        self.name = name
        self.email = email
        self.time = time
        self.room = room
