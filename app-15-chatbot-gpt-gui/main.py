from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600, 400)

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


        self.show()


class Chatbot:
    pass

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())