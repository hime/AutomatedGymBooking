# user class with all user data
class GymUser:
    name: str
    email: str
    room_number: str
    def __init__(self, name: str, email: str, room_number: int):
        self.name = name
        self.email = email
        self.room_number = room_number
