import os
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail
from config import Config


def send_email(sendgrid_api_key, from_email, to_email, botname, results):
    sg = sendgrid.SendGridAPIClient(
        apikey = sendgrid_api_key
    )
    from_email = Email(from_email)
    to_email = Email(to_email)
    subject = botname
    content = Content("text/plain", results)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response)

def main():
    config = Config('config.toml')
    config.parseConfigs()
    botname: str = config['bot']['botname']
    sendgrid_api_key: str = config['api_credentials']['sendgrid_api_key']
    from_email: str = config['notifications']['from_email']
    to_email: str = config['notifications']['to_email']

if __name__ == "__main__":
    main()
