import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Chatbot:
    def __init__(self):
        # Set the API key from the .env file
        openai.api_key = os.getenv("OPENAI_API")
        if not openai.api_key:
            raise ValueError("API key not set in .env file.")

    def get_response(self, user_input):
        try:
            # Use the recommended chat model
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=3000,
                temperature=0.5
            )
            # Return the response text
            return response.choices[0].message['content'].strip()
        except Exception as e:
            return f"An error occurred: {e}"

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Tell me a joke")
    print(response)
