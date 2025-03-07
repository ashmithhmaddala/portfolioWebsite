import smtplib
import ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "ashmith.maddala@gmail.com"
    password = os.getenv(${{ secrets.GMAIL_PASSWORD }})

    if not password:
        print("Error: GMAIL_PASSWORD is not set.")
        return

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, username, message)
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
