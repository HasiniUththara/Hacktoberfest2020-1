import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    email = "<< Enter your email here >>"
    password = "<< Enter your password here>>"
    to = "<< Enter sender email >>"
    msg = """ << Email Body >>"""
    message = MIMEMultipart()
    message["From"] = email
    message["To"] = to
    message["Subject"] = "HacktoberFest 2020"
    message.attach(MIMEText(msg, "plain"))
    context = ssl.create_default_context()
    server = smtplib.SMTP("smtp.gmail.com")
    server.starttls()
    server.ehlo()
    server.login(email, password)
    server.sendmail(email, to, message.as_string())
    print('Your Email have been successfully send')

except Exception as ex:
    print(ex)

finally:
    server.quit()
© 2020 GitHub, Inc.
