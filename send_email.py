import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "freja400d@gmail.com"
receiver_email = "freja400d@gmail.com"
password = "qksidrofwqyfmooi"

message = MIMEMultipart("alternative")
message["Subject"] = "Twitter signup"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Welcome!,
Thank you for signing up to my Twitter!
www.your_website_here.com"""
html = """\
<html>
  <body>
    <p style="font-size: 24px; margin-bottom: 0">Welcome!
    <p> Thank you for signing up to my Twitter!</p>
       <a href="https://pandapoob.eu.pythonanywhere.com/">Go to Twitter</a>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )