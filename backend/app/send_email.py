import aiosmtplib
from email.message import EmailMessage

async def send_email(to: str, subject: str, body: str):
    message = EmailMessage()
    message["From"] = "your_email@example.com"
    message["To"] = to
    message["Subject"] = subject
    message.set_content(body)

    await aiosmtplib.send(message, hostname="smtp.example.com",
                          port=587, username="your_email@example.com", password="your_password", start_tls=True)