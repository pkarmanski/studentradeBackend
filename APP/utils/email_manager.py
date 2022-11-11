from email.message import EmailMessage
import ssl
import smtplib

email_password = "vsequzzctneentlx"


def create_mail_data(email_receiver: str, subject: str, body: str):
    email_sender = "studentrade.management@gmail.com"
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

