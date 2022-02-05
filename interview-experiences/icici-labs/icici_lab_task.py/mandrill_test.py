import mandrill
import os

class Mandrill:
    def send_message(self,to_addr,email_sub,email_body):
        mandrill_client = mandrill.Mandrill(os.environ.get('MANDRILL_API_KEY'))
        message = {
        'to': [{
            'email': to_addr,
            'type': 'to'
        }],
        'subject': email_sub,
        'text': email_body
        }
        mandrill_client.messages.send(message = message)