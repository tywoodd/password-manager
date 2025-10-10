from PySide6.QtWidgets import QDialog, QLineEdit
from PySide6.QtCore import Signal, Qt
from .ui_entry_editor import Ui_EntryEditorDialog
import secrets
import string



class EntryEditor(QDialog, Ui_EntryEditorDialog):
    saved = Signal(dict)

    def __init__(self, mode: str = "create", entry: dict | None = None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mode = mode
        self._entry = entry or {}

        if mode == "edit":
            self.setWindowTitle("Edit Entry")
            self.titleEdit.setText(entry["title"])
            self.usernameEdit.setText(entry["username"])
            self.uRLEdit.setText(entry["url"])
            self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
            self.notesEdit.setText(entry["notes"])
        else:
            self.setWindowTitle("New Entry")
            self.passwordHintLabel.clear()
            self.passwordEdit.clear()
            self.retypePasswordEdit.clear()
            self.titleEdit.clear()
            

        # Disable "Save" button by default 
        self.save_btn = self.buttonBox.button(self.buttonBox.StandardButton.Save)
        self.save_btn.setEnabled(False)


        # ---------- Tool Buttons -------------------


        # Toggle Password button
        self.togglePwdButton.setCheckable(True)
        self.togglePwdButton.toggled.connect(self.toggle_password_view)

        # Toggle Password retype button
        self.togglePwdButton2.setCheckable(True)
        self.togglePwdButton2.toggled.connect(self.toggle_password2_view)

        # Generate Password button
        self.generatePwdButton.clicked.connect(self.generate_password)

        # --------------------------------------------

        # Signals
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.passwordEdit.textChanged.connect(self._validate_form)
        self.retypePasswordEdit.textChanged.connect(self._validate_form)



    # Check if form is valid - All fields are filled - Passwords match - Password is 8+ characters
    def _validate_form(self):
        password = self.passwordEdit.text().strip()
        retype = self.retypePasswordEdit.text().strip()
        username = self.usernameEdit.text().strip()

        if not username or not password or not retype:
            self.passwordHintLabel.setText("All fields are required.")
            self.passwordHintLabel.setStyleSheet("color: red;")
            self.save_btn.setEnabled(False)
            return
        
        if password != retype:
            self.passwordHintLabel.setText("Passwords do not match.")
            self.passwordHintLabel.setStyleSheet("color: red;")
            self.save_btn.setEnabled(False)
            return

        if len(password) < 8:
            self.passwordHintLabel.setText("Password must be at least 8 characters.")
            self.passwordHintLabel.setStyleSheet("color: red;")
            self.save_btn.setEnabled(False)
            return

        self.passwordHintLabel.clear()
        self.save_btn.setEnabled(True)


   #Returns data from dialog for the Entry Payload 
    def get_data(self) -> dict:
        return {
            "title": self.titleEdit.text().strip(),
            "username": self.usernameEdit.text().strip(),
            "password": self.passwordEdit.text().strip(),
            "password2":self.retypePasswordEdit.text().strip(),
            "url": self.uRLEdit.text().strip(),
            "notes": self.notesEdit.toPlainText()
        }
    

    # Toggle Password view Method
    def toggle_password_view(self, checked):
        if checked:
            self.passwordEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(QLineEdit.Password)


    # Toggle Password retype view Method
    def toggle_password2_view(self, checked):
        if checked:
            self.retypePasswordEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.retypePasswordEdit.setEchoMode(QLineEdit.Password)


    # Generate new password
    def generate_password(self):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(22))
        self.passwordEdit.setText(password)
        self.retypePasswordEdit.setText(password)