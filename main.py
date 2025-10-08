from core.db import init_db, SessionLocal
from core.vault_service import VaultService
from ui.main_window import MainWindow
from ui.models.vault_table import VaultTableModel
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
import sys


def main():
    # DB + Policy boostrap
    init_db()
    session = SessionLocal()

    # Create App, Vault, Window
    app = QApplication(sys.argv)
    vault = VaultService(session)
    window = MainWindow(app, vault)


    # ------- Unlocks Vault with Master Password + Shows Entries Table page -------
    def unlock_vault():
        master_password = window.passwordEdit.text().strip()
        
        try:
            vault.unlock(master_password)

        except Exception:
            window.unlockHintLabel.setText("Incorrect Password")
            QTimer.singleShot(3000, lambda: window.unlockHintLabel.setText(""))

        else:
            entries = vault.list_entries()
            model = VaultTableModel(entries)
            window.table.setModel(model)
            window.unlock_vault()


    window.unlockButton.clicked.connect(unlock_vault)
    window.passwordEdit.returnPressed.connect(unlock_vault)

    window.show()    
    app.exec() 


if __name__ == "__main__":
    main()


# TODO 
# 
# 
# 
# 
# 
#  create -- edit_entry(self) -- method for the VaultService
#  so that edit_entry can update the db, rather than create a new entry
# .
# 
#
#
# 
# 
# 
# 
# 
# 
# 
# .
