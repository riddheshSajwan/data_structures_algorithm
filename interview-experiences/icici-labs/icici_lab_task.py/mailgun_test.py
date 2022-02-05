import os
import requests

class MailGun:
    def send_message(self,to_addr,email_sub,email_body):
        return requests.post(
            "https://api.mailgun.net/v3/sandbox00e7d863440f441aac7e1f3c7a042f8f.mailgun.org/messages",
            auth=("api", os.environ.get('MAILGUN_API_KEY')),
            data={"from": "Riddhesh Sajwan <riddhesh10@gmail.com>",
                "to": [to_addr],
                "subject": email_sub,
                "text": email_body})
