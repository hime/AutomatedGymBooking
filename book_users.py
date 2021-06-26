# Jaime Bohorquez
# Programmed using Atom + iTerm2 on Mac OS Big Sur
# Filename: create_booking

# Whenever this script runs, we get our users from the UserInfo.JSON and send
# post requests for a booking.

from gym_requests import GymRequest
from user import GymUser as User
import json

# For obvious reasons this file was .gitignored.
# See example file to create your own.
file_info = open('./json/UserInfo.JSON', encoding='utf-8')
data = json.load(file_info)
users = []
json_users = data["users"]

for json_user in json_users:
    users.append(User(
            name=json_user["name"],
            email=json_user["email"],
            time=json_user["time"],
            room=json_user["room"]
        )
    )

attempts = 0
limit_of_attempts = 30
for user in users:
    req = GymRequest(user)
    while attempts < limit_of_attempts:
        resp = req.post_request()
        if "Booking" in resp.json():
            print("Booked for", user.name, "at", user.time + ".")
            break
        print("Retrying...")
        attempts += 1
    if attempts == limit_of_attempts:
        print("Failed to book for", user.name, "at", user.time + ".")
