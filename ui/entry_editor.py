from PySide6.QtWidgets import QDialog, QLineEdit
from PySide6.QtCore import Signal, Qt
from .ui_entry_editor import Ui_EntryEditorDialog



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

        # Signals
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.passwordEdit.textChanged.connect(self._validate_form)
        self.retypePasswordEdit.textChanged.connect(self._validate_form)


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

    
    def get_data(self) -> dict:
        return {
            "title": self.titleEdit.text().strip(),
            "username": self.usernameEdit.text().strip(),
            "password": self.passwordEdit.text().strip(),
            "password2":self.retypePasswordEdit.text().strip(),
            "url": self.uRLEdit.text().strip(),
            "notes": self.notesEdit.toPlainText()
        }