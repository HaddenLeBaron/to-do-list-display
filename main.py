from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QStackedWidget


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
stack = QStackedWidget()

#
# label = QLabel("To Do")
# layout.addWidget(label)
#
# btn = QPushButton("Tap me")
# layout.addWidget(btn)
#
# def on_click():
#     print("Button pressed!")
#
# btn.clicked.connect(on_click)

def make_page(title, button_text, button_action):
    """Utility to create a simple page."""
    page = QWidget()
    layout = QVBoxLayout(page)
    label = QLabel(title)
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet("font-size: 32px;")
    button = QPushButton(button_text)
    # button.setStyleSheet("font-size: 24px; padding: 10px;")
    button.clicked.connect(button_action)
    layout.addWidget(label)
    layout.addWidget(button)
    return page

def show_completed():
    stack.setCurrentIndex(1)

def show_todo():
    stack.setCurrentIndex(0)

todo_list = make_page('To-Do list', 'Go to Completed', show_completed)
completed_list = make_page('Completed Tasks', 'Back to Todo', show_todo)


stack.addWidget(todo_list)
stack.addWidget(completed_list)
stack.setCurrentIndex(0)


layout.addWidget(stack)
window.setLayout(layout)
window.show()

# window.setWindowFlags(Qt.FramelessWindowHint)
# window.showFullScreen()

app.exec()



