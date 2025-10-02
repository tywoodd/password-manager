from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QSlider, QToolBar, QLabel, QLineEdit
from PySide6.QtCore import Qt, QSize, QTimer
from .ui_mainwindow import Ui_MainWindow
from . import resources_rc as resources_rc  
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.toolBar.hide()

        self.setWindowTitle("Vault")

        # Unlock Button
        self.unlockButton.clicked.connect(self.return_password_text)
        self.passwordEdit.returnPressed.connect(self.return_password_text)

        # Lock Button
        self.actionLock.triggered.connect(self.lock_vault)

        # Entries Table
        self.table = self.entriesTable
        self._model = None


    def set_model(self, model):
        self._model = model
        self.table.setModel(model)

    def return_password_text(self):
        return self.passwordEdit.text()

    def unlock_vault(self):
        self.passwordEdit.clear()
        self.stackedWidget.setCurrentIndex(1)
        self.toolBar.show()

    def lock_vault(self):
        self.stackedWidget.setCurrentIndex(0)
        self.toolBar.hide()

    def quit_app(self):
        self.app.quit()
