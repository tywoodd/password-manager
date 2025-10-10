from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QSlider, QToolBar, QLabel, QLineEdit, QMessageBox
from PySide6.QtCore import Qt, QSize, QTimer, QRegularExpression, QSortFilterProxyModel
from PySide6.QtGui import QGuiApplication, QClipboard
from ui.models.vault_table import VaultTableModel
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
        self.model = None

        # Table Search
        self.proxy = QSortFilterProxyModel(self)
        self.proxy.setFilterKeyColumn(-1)
        self.table.setModel(self.proxy)

        self.searchEdit.textChanged.connect(self.search_filter)

        # Toolbar Buttons
        self.actionNew.triggered.connect(self.on_new_entry)
        self.actionEdit.triggered.connect(self.on_edit_entry)
        self.action_Delete.triggered.connect(self.on_delete)
        self.actionLock.triggered.connect(self.lock_vault)

        # Unlock Vault Button
        self.unlockButton.clicked.connect(self.return_password_text)
        self.passwordEdit.returnPressed.connect(self.return_password_text)

        # Double Click to Copy
        self.table.doubleClicked.connect(self.double_click)


    # -------------- Entries Table Methods -----------------------


    # Table Model Method
    def set_model(self, model):
        self.model = model
        self.proxy.setSourceModel(self.model)


    # Table Search Method
    def search_filter(self, text):
        search = QRegularExpression(QRegularExpression.escape(text), QRegularExpression.CaseInsensitiveOption)
        self.proxy.setFilterRegularExpression(search)


    # Select Row Method
    def selected_entry_id(self) -> str | None:
        selected_rows_list = self.table.selectionModel().selectedRows()
        if not selected_rows_list:
            return None
        row = selected_rows_list[0].row()
        entry_uuid = self.table.model().index(row, 0)
        return entry_uuid.data()


    # Double Click Method
    def double_click(self, index):
        if not index.isValid():
            return
        
        model = index.model() or self.table.model()
        if model is None:
            return

        value = model.data(index, Qt.DisplayRole)
        if not value:
            return
        
        if index.column() == 3:
            entry = model._entries[index.row()]
            value = entry["password"]

        QApplication.clipboard().setText(value)


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
            entries = self.vault.list_entries()
            self.model = VaultTableModel(entries)
            self.proxy.setSourceModel(self.model)
            self.table.setModel(self.proxy)


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

        dlg._validate_form()
        self.vault.update_entry(
            entry_id=entry_id,
            title=data.get("title"),
            username=data.get("username"),
            password=data.get("password"),
            url=data.get("url"),
            notes=data.get("notes")
        )
        entries = self.vault.list_entries()
        self.model = VaultTableModel(entries)
        self.proxy.setSourceModel(self.model)
        self.table.setModel(self.proxy)


    # Delete Entry Method
    def on_delete(self):
        reply = QMessageBox.question(
            self,
            "Confirm Deletion",
            "Are you sure you want to delete?",
            QMessageBox.Yes | QMessageBox.Cancel
        )
        
        if reply == QMessageBox.Yes:
            entry_id = self.selected_entry_id()
            self.vault.delete_entry(entry_id)        
            entries = self.vault.list_entries()
            self.model = VaultTableModel(entries)
            self.proxy.setSourceModel(self.model)
            self.table.setModel(self.proxy)
        else:
            return


    # Lock Vault Method
    def lock_vault(self):
        self.vault.lock()
        self.stackedWidget.setCurrentIndex(0)
        self.toolBar.hide()


    # -------------- Unlock Vault Method ------------------

    def unlock_vault(self):
        master_password = self.passwordEdit.text().strip()
        
        try:
            self.vault.unlock(master_password)

        except Exception:
            self.unlockHintLabel.setText("Incorrect Password")
            QTimer.singleShot(3000, lambda: self.unlockHintLabel.setText(""))

        else:
            entries = self.vault.list_entries()
            self.model = VaultTableModel(entries)
            self.proxy.setSourceModel(self.model)
            self.table.setModel(self.proxy)

            self.passwordEdit.clear()
            self.table.setColumnHidden(0, True) 
            self.stackedWidget.setCurrentIndex(1)
            self.toolBar.show()


    def return_password_text(self):
        return self.passwordEdit.text()
