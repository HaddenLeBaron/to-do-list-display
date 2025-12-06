from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QStackedWidget,
                               QTableWidget, QTableWidgetItem, QCheckBox, QSizePolicy, QHBoxLayout)
from todoist_api_python.api import TodoistAPI


app = QApplication([])
window = QWidget()
main_layout = QVBoxLayout()
stack = QStackedWidget()

api = TodoistAPI("afd09492def59fe7e927e7e5f1ac6edb25b165dc")
project_id = '6fHmMp9vx55g7fmf'

to_do_list = []

try:
    package = api.get_tasks(project_id=project_id)

    for p in package:
        for task in p:
            to_do_list.append((task.content, task.is_completed))
except Exception as e:
    print("Error:", e)


def make_page(title, button_text, button_action, qtable=None):
    """Utility to create a simple page."""
    page = QWidget()
    layout = QVBoxLayout(page)
    label = QLabel(title)
    # label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet("font-size: 32px;")
    button = QPushButton(button_text)
    button.setStyleSheet("font-size: 24px; padding: 10px;")
    button.clicked.connect(button_action)
    layout.addWidget(label)
    if qtable:
        layout.addWidget(qtable)
    layout.addWidget(button)
    return page

def show_completed():
    stack.setCurrentIndex(1)

def show_todo():
    stack.setCurrentIndex(0)

# data = ["dishes", "floors", "trash", "fridge", "wipe counters", "make dinner", "check mail", "walk dog", "change sheets", "laundry"]
table = QTableWidget(len(to_do_list), 2)
table.setStyleSheet("""
                    QTableWidget {font-size: 24px;}
                    QTableWidget::item {
                        padding-left: 7px;
                    }""")

table.setColumnWidth(0, 50)
table.setColumnWidth(1, 696)

table.verticalHeader().setVisible(False)
table.horizontalHeader().setVisible(False)

for i in range(len(to_do_list)):
    checkbox = QCheckBox()
    checkbox.setStyleSheet("""
    QCheckBox::indicator {
        width: 40px;
        height: 40px;
        image: url(unchecked.png)
    }
    QCheckBox::indicator:checked {
        image: url(checkmark.png);
    }
    
    """)
    checkbox_widget = QWidget()
    checkbox_widget.setMinimumSize(30, 30)

    layout = QHBoxLayout(checkbox_widget)
    layout.addWidget(checkbox)
    layout.setAlignment(Qt.AlignCenter)
    layout.setContentsMargins(0, 0, 0, 0)
    table.setRowHeight(i, 50)
    table.setCellWidget(i, 0, checkbox_widget)
    table.setItem(i, 1, QTableWidgetItem(to_do_list[i][0]))



todo_list = make_page('To-Do list', 'Go to Completed', show_completed, table)
completed_list = make_page('Completed Tasks', 'Back to Todo', show_todo)


stack.addWidget(todo_list)
stack.addWidget(completed_list)
stack.setCurrentIndex(0)

main_layout.addWidget(stack)
window.setLayout(main_layout)
window.resize(800, 480)
window.show()


app.exec()

# possibly helpful when actually on raspberry pi
# window.setWindowFlags(Qt.FramelessWindowHint)
# window.showFullScreen()
