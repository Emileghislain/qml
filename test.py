from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize, Qt
import sys

from random import choice

window_titles = [
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_check = True
        self.setWindowTitle("Test")
        self.setFixedSize(QSize(400, 300))
        self.button = QPushButton('Push Me')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.click)

        self.setCentralWidget(self.button)

        self.windowTitleChanged.connect(self.window_title_change)

    def click(self):
        self.button.setText('Push Me')
        new_window = choice(window_titles)
        self.setWindowTitle(new_window)

    def window_title_change(self, window_title):
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()