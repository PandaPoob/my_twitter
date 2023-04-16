import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(receiver_email, user_api_key):
 
    sender_email = "freja400d@gmail.com"
    password = "qksidrofwqyfmooi"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Freja's exam's site signup"
    message["From"] = sender_email
    message["To"] = receiver_email

    try:
        import production
        root = "https://pandapoob.eu.pythonanywhere.com/"
    except:
        root = "http://127.0.0.1:3000/"

    # Create the plain-text and HTML version of your message
    text = """\
    Welcome!,
    Thank you for signing up to my exam project!"""
    html = f"""\
    <html>
      <body style="background-color: black; color: white; padding: 12px; border-radius: 10px; text-align: center">
        <p style="font-size: 24px; margin-bottom: 0; margin-top: 4px">Welcome!</p>
        <p>Thank you for signing up to my Project! You can click the link below to verify your account</p>
           <a style="background-color: #1d9bf0; font-size: 16px; font-weight: bold; padding-right: 16px; padding-left: 16px; padding-top: 12px; padding-bottom: 12px; color: white; text-decoration: none; border-radius: 30px; margin-bottom: 16px; text-align: center" 
           href="{root+"verify-user/"+user_api_key}">Verify account</a>
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