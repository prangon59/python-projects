import smtplib
import ssl
import requests
import selectorlib
from dotenv import load_dotenv
import os

load_dotenv()

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    response = requests.get(url)
    source_code = response.text
    return source_code


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "twintidebd@gmail.com"
    password = os.getenv("APP_PASSWORD")
    reciever = "twintidebd@gmail.com"
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)
    print("Email sent!")


def store_data(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read_data(extracted):
    with open("data.txt", "r") as file:
        return file.read()
        

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

    content = read_data(extracted)
    if extracted != "No upcoming tours":
        if extracted not in content:
            store_data(extracted)
            send_email(message="New event found.")