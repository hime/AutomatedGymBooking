# Automated Gym Booking
## What Does This Do?
This automatically books my gym visit through outlook.
## Why Am I Doing This?
Well you see, Facebook corporate housing in NY has a very small gym. Aside from that, since Covid is still a thing, you need to reserve the gym. Unless you stay up until midnight to race someone to fill the booking, you aren't getting a slot. With this, I can now sleep peacefully knowing I will get a slot for myself. #learntocode
## Running on Schedule
We want to start sending requests (until we get a 200 status) at midnight.
```sh
./create booking | at 00:00
```
