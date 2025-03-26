import smtplib, ssl
from email.message import EmailMessage

def sendEmail(receiver, message):
    host = "smtp.gmail.com"
    port = 465

    # Load credentials from environment variables (SECURE!)
    subject = "Expo25 Escape Room Results"
    username = "expo25.mhse@gmail.com"
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = username
    password = "xjkx vohf zdcz zwad"
    msg["To"] = receiver
    msg.set_content(message)

    if not username or not password:
        print("❌ ERROR: Email credentials are missing!")
        return False

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.send_message(msg)
        print(f"✅ Email sent successfully to {receiver}")
        return True

    except smtplib.SMTPAuthenticationError:
        print("❌ ERROR: Authentication failed. Check your email and password.")
    except smtplib.SMTPException as e:
        print(f"❌ ERROR: Email sending failed - {e}")
    
    return False
