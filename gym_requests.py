import json
import requests
from user import GymUser as User

class GymRequest:
    user: User
    url: str = 'https://outlook.office365.com/owa/calendar/AKATimesSquare@korman.onmicrosoft.com/bookings/service.svc/CreateBooking'
    def __init__(self, user):
        self.user = user

    def get_payload(self):
        return {
            "ServiceId":"8C5q1gaOYE2I1uTup8Jg3A2",
            "RequiredSlotCount":1,
            "AnsweredQuestionList":
            [
                {
                    "Question":"Suite No",
                    "Id":"b7858409-6dd8-4600-b7a7-d87105275fc8",
                    "Required":True,
                    "Answer":"808"
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
            "Start":"2021-06-27T11:00:00",
            "StaffList":["WhCwT8QaG0CMrDeyfpjM3Q=="],
            "CustomerName":"Jaime",
            "CustomerEmail":"bambas@knights.ucf.edu",
            "CustomerLocation":"",
            "PrivacyPolicyConsented": True,
            "TermsAndConditionsConsented": True
        }
    def post_request(self):
        payload = self.get_payload()
        response = requests.post(self.url, data=json.dumps(payload))
        return response
