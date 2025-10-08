from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QSlider, QToolBar, QLabel, QLineEdit
from PySide6.QtCore import Qt, QSize, QTimer
from .ui_mainwindow import Ui_MainWindow
from .entry_editor import EntryEditor
from . import resources_rc as resources_rc  
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app, vault_service):
        super().__init__()
        self.app = app
        self.vault = vault_service
        self.setWindowTitle("Vault")
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.toolBar.hide()

        # Entries Table
        self.table = self.entriesTable
        self._model = None

        # Toolbar Buttons
        self.actionNew.triggered.connect(self.on_new_entry)
        self.actionEdit.triggered.connect(self.on_edit_entry)
        self.action_Delete.triggered.connect(self.on_delete)
        self.actionLock.triggered.connect(self.lock_vault)

        self.table.doubleClicked.connect(self.on_edit_entry)

        # Unlock Vault Button
        self.unlockButton.clicked.connect(self.return_password_text)
        self.passwordEdit.returnPressed.connect(self.return_password_text)


    # -------------- Entries Table Methods -----------------------


    # Table Model Method
    def set_model(self, model):
        self._model = model
        self.table.setModel(model)


    # Select Row Method
    def selected_entry_id(self) -> str | None:
        selected_rows_list = self.table.selectionModel().selectedRows()
        if not selected_rows_list:
            return None
        row = selected_rows_list[0].row()
        entry_uuid = self.table.model().index(row, 0)
        return entry_uuid.data()


    # -------------- Toolbar Methods ------------------


    # New Entry Method
    def on_new_entry(self):
        dlg = EntryEditor(mode="create", parent=self)
        if not dlg.exec():
            return
        data = dlg.get_data()

        if data.get("password") != data.get("password2"):
            dlg.passwordHintLabel.setText("Passwords must match")
            QTimer.singleShot(3000, lambda: dlg.passwordHintLabel.setText(""))

        else:
            dlg._validate_form()
            self.vault.write_entry(
                title=data.get("title"),
                username=data.get("username"),
                password=data.get("password"),
                url=data.get("url"),
                notes=data.get("notes")
            )

    # Edit Entry Method
    def on_edit_entry(self):
        entry_id = self.selected_entry_id()
        if entry_id is None:
            return
        
        entry = self.vault.read_entry(entry_id)
        dlg = EntryEditor(mode="edit", parent=self, entry=entry)
        if not dlg.exec():
            return
        data = dlg.get_data()

        if data.get("password") != data.get("password2"):
            dlg.passwordHintLabel.setText("Passwords must match")
            QTimer.singleShot(3000, lambda: dlg.passwordHintLabel.setText(""))

        else:
            dlg._validate_form()
            self.vault.update_entry(
                entry_id=entry_id,
                title=data.get("title"),
                username=data.get("username"),
                password=data.get("password"),
                url=data.get("url"),
                notes=data.get("notes")
            )


    # Delete Entry Method
    def on_delete(self):
        entry_id = self.selected_entry_id()
        if entry_id is None:
            return
        pass


    # Lock Vault Method
    def lock_vault(self):
        self.stackedWidget.setCurrentIndex(0)
        self.toolBar.hide()


    # -------------- Unlock Vault Method ------------------

    def unlock_vault(self):
        self.passwordEdit.clear()
        self.table.setColumnHidden(0, True) 
        self.stackedWidget.setCurrentIndex(1)
        self.toolBar.show()


    def return_password_text(self):
        return self.passwordEdit.text()
