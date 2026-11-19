from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5.uic import loadUi
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        loadUi('customized_widget.ui',self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    app.exec_()