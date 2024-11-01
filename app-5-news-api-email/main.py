import requests
import os
from dotenv import load_dotenv
from send_email import send_email

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={api_key}"

request = requests.get(url)
content = request.json()

body = ""
for articles in content["articles"]:
    if articles["title"] is not None:
        body = body + articles["title"] + "\n" + articles["description"] + 2*"\n"

send_email(body)

