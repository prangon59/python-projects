import requests
import os
from dotenv import load_dotenv
from send_email import send_email

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("NEWS_API_KEY")

topic = "bitcoin"
url = f"https://newsapi.org/v2/everything?q={topic}&language=en&apiKey={api_key}"

request = requests.get(url)
content = request.json()

body = "Subject: Today's Hot News\n\n"
for articles in content["articles"][:10]:
    if articles["title"] is not None:
        body += (
            articles["title"] + "\n" 
            + (articles["description"] or "No description available.") + "\n"
            + articles["url"] + "\n\n"
        )

body = body.encode("utf-8")
send_email(body)

