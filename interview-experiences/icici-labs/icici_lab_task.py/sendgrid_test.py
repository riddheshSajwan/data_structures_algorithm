import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class SendGrid:
    def send_message(self,to_addr,email_sub,email_body):
        message = Mail(
            from_email='riddhesh10@gmail.com',
            to_emails=to_addr,
            subject=email_sub,
            html_content=email_body)
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
