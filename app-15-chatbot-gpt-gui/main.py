from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys
from backend import Chatbot

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 400)

        # Initialize chatbot
        self.chatbot = Chatbot()

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 580, 200)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 220, 500, 80)


        # Add the button widget
        self.button = QPushButton("Send", self)
        self.button.setGeometry(520, 220, 70, 80)
        self.button.clicked.connect(self.send_message)  # Connect button to the method

        self.show()

    def send_message(self):
        user_input = self.input_field.text()
        if user_input.strip():  # Ensure input isn't empty
            self.chat_area.append(f"You: {user_input}")
            response = self.chatbot.get_response(user_input)
            self.chat_area.append(f"Bot: {response}")
            self.input_field.clear()  # Clear input field after sending

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())