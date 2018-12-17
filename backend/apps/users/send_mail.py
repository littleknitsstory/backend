import sendgrid
from sendgrid.helpers.mail import *
from django.conf import settings
SENDGRID_API_KEY = settings.SENDGRID_API_KEY


class SendEmail:
    def __init__(self, from_email, to_email, subject, content):
        self.from_email = Email(from_email)
        self.to_email = Email(to_email)
        self.subject = subject
        self.content = Content("text/plain", content)

    def send(self):
        sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
        mail = Mail(self.from_email, self.subject, self.to_email, self.content)
        response = sg.client.mail.send.post(request_body=mail.get())
        return response

