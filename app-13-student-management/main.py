from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QGridLayout, \
    QWidget, QLabel, QLineEdit, QPushButton, QMainWindow, \
    QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, \
    QComboBox, QToolBar, QStatusBar, QMessageBox
import sys
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800, 600)

        file_menu_item = self.menuBar().addMenu("&File")
        edit_menu_item = self.menuBar().addMenu("&Edit")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction(QIcon("icons\\add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)   
        help_menu_item.addAction(about_action)
        about_action.triggered.connect(self.about)

        search_action = QAction(QIcon("icons\\search.png"), "Search", self)
        search_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)


        # Create toolbar and add toolbar elements
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # Create status bar and add it's elements
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        # Detect a clicked cell
        self.table.cellClicked.connect(self.cell_clicked)

        self.load_data()

    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)


    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()
    
    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()

    def about(self):
        dialog = AboutDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        layout = QVBoxLayout()

        # Add student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # Add Mobile Number input box
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        # Add a submit button
        button = QPushButton("Submit")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)
        
        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        layout = QVBoxLayout()

        # Add search action dialog
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Search Here")
        layout.addWidget(self.student_name)

        # Create Button
        button = QPushButton("Search")
        button.clicked.connect(self.perform_search)
        layout.addWidget(button)

        self.setLayout(layout)

    def perform_search(self):
         # Logic for searching in the database
        name = self.student_name.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        results = list(cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',)))
        print(results)
        items = main_window.table.findItems(name, Qt.MatchFlag.MatchContains)
        for item in items:
            print(item)
            # Print or process results (you can display them in a table or another dialog)
            print(f"Search results for '{name}': {results}")
            main_window.table.item(item.row(), 1).setSelected(True)
        cursor.close()
        connection.close()


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        layout = QVBoxLayout()

        # Get sudent name from selected row
        index = main_window.table.currentRow()
        self.student_id = main_window.table.item(index, 0).text()
        student_name = main_window.table.item(index, 1).text()
        course_name = main_window.table.item(index, 2).text()  # Course is in column 2
        mobile_number = main_window.table.item(index, 3).text()  # Mobile is in column 3

        # Add student name widget
        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course_name)
        layout.addWidget(self.course_name)

        # Add Mobile Number input box
        self.mobile = QLineEdit(mobile_number)
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        # Add a submit button
        button = QPushButton("Update")
        button.clicked.connect(self.update_student_info)
        layout.addWidget(button)
        
        self.setLayout(layout)

    def update_student_info(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?", 
                        (self.student_name.text(), 
                        self.course_name.itemText(self.course_name.currentIndex()), 
                        self.mobile.text(), 
                        self.student_id))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data() # Refreshes the table


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")

        layout = QGridLayout()
        confirm_message = QLabel("Are you sure you want to delete?")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        layout.addWidget(confirm_message, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout)

        yes.clicked.connect(self.delete_student)

    def delete_student(self):
        index = main_window.table.currentRow()
        student_id = main_window.table.item(index, 0).text()

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("DELETE from students WHERE id = ?", (student_id,))
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()
        
        self.close()

        confirm_widget = QMessageBox()
        confirm_widget.setWindowTitle("Success")
        confirm_widget.setText("The record deleted successfully.")
        confirm_widget.exec()


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = '''i created this app while doing the course of pyhton mega course from udemy. 
        It was a really nice course to do and learn along the way'''
        self.setText(content)

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())