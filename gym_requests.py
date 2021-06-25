# Jaime Bohorquez
# Programmed using Atom + iTerm2 on Mac OS Big Sur
# Filename: gym_requests.py

import json
import requests
import datetime
from user import GymUser as User

class GymRequest:
    user: User
    url: str = 'https://outlook.office365.com/owa/calendar/AKATimesSquare@korman.onmicrosoft.com/bookings/service.svc/CreateBooking'
    def __init__(self, user):
        self.user = user
    def _get_month_days(self, date):
        file_info = open('./json/months-detailed.JSON', encoding='utf-8')
        data = json.load(file_info)
        total_days = 0
        for month in data["month_data"]:
            if month["number"] < date.month:
                total_days += month["days"]
            if month["number"] == 2 and date.year % 4 == 0:
                total_days += 1
        return total_days

    def _add_days(self, days):
        date = datetime.date.today()
        day = date.day
        month_days = self._get_month_days(date)
        year = date.year
        next_booking_day = day + month_days + days
        year_limit = 365 if year % 4 else 366
        if next_booking_day > year_limit:
            next_booking_day %= year_limit
            year += 1
        return (next_booking_day, year)

    def _get_payload(self):
        datetime.date
        (day_of_year, year) = self._add_days(2)
        date = datetime.datetime.strptime(
            str(year) + ' ' + str(day_of_year), '%Y %j'
        ).strftime('%Y-%m-%d')
        return {
            "ServiceId":"8C5q1gaOYE2I1uTup8Jg3A2",
            "RequiredSlotCount":1,
            "AnsweredQuestionList":
            [
                {
                    "Question":"Suite No",
                    "Id":"b7858409-6dd8-4600-b7a7-d87105275fc8",
                    "Required":True,
                    "Answer":self.user.room
                },
                {
                    "Question":"Please complete the COVID-19 symptom screening questions mandated by the New York State Department of Health attached to your appointment confirmation email reminder that will be sent 2 hours prior to your appointment time. ",
                    "Id":"63f33fda-4905-4b21-8c6a-eeabe33094be",
                    "Required":True,
                    "Options":
                    ["I agree","I decline (your booking will be cancelled)"],
                    "SelectedOptions":[0],
                    "Answer":"I agree"
                }
            ],
            "Start":date+"T"+self.user.time,
            "StaffList":["WhCwT8QaG0CMrDeyfpjM3Q=="],
            "CustomerName":self.user.name,
            "CustomerEmail":self.user.email,
            "CustomerLocation":"",
            "PrivacyPolicyConsented": True,
            "TermsAndConditionsConsented": True
        }
    def post_request(self):
        payload = self._get_payload()
        response = requests.post(self.url, data=json.dumps(payload))
        return response
