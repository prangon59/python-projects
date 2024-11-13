import smtplib
import mimetypes
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv("APP_PASSWORD")
SENDER = "twintidebd@gmail.com"
RECIEVER = "twintidebd@gmail.com"

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer.")

    # Determine the mimetype and subtype of the file
    mime_type, _ = mimetypes.guess_type(image_path)
    maintype, subtype = mime_type.split('/')

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype=maintype, subtype=subtype, filename=os.path.basename(image_path))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECIEVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/19.png")