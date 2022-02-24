'''
Task:
Create a service that accepts the necessary information and sends emails. It should
provide an abstraction between two different email service providers. If one of the
services goes down, your service can quickly failover to a different provider without
affecting your customers.
Example Email Providers:
● SendGrid
● Mailgun
● Mandrill
● Amazon SES
All listed services are free to try and are pretty painless to sign up for, so please register
your own test accounts on each.

Evaluation Criteria (What we look for in your code?)
1. Code Readability and Organisation. (How easy is it to read and understand your
code?)
2. API calls and Data usage (How are you calling the API endpoints?)
3. Code Reusability (How structured and reusable is your code?)
4. Necessary Validations (How are you checking for possible errors in your code?)
5. Bonus: Testing (How reliable is your code?)
'''
from sendgrid_test import SendGrid
from mailgun_test import MailGun
from mandrill_test import Mandrill

class SendMail:
    def main(self):
        to_addr = input("Receiver Address: ")
        email_sub = input("Subject of your mail: ")
        email_body = input("Body of your mail: ")
        service_providers = {"Mandrill":Mandrill(),"SendGrid":SendGrid(),"MailGun":MailGun()}
        for service_provider in service_providers:
            try:
                service_providers[service_provider].send_message(to_addr,email_sub,email_body)
                print("Email was sent via {}".format(service_provider))
                break
            except:
                print("{} is down, we will attempt to send it via some other provider".format(service_provider))


if __name__ == "__main__":
    SendMail().main()

'''
Sample Output:

Receiver Address: riddhesh10@gmail.com
Subject of your mail: sub
Body of your mail: body
Mandrill is down, we will attempt to send it via some other provider
Email was sent via SendGrid

'''