from core.db import init_db, SessionLocal
from core.vault_service import VaultService
from ui.main_window import MainWindow
from PySide6.QtWidgets import QApplication
import sys


def main():
    # DB + Policy boostrap
    init_db()
    session = SessionLocal()

    # Create App, Vault, Window
    app = QApplication(sys.argv)
    vault = VaultService(session)
    window = MainWindow(app, vault)

    window.unlockButton.clicked.connect(window.unlock_vault)
    window.passwordEdit.returnPressed.connect(window.unlock_vault)

    window.show()    
    app.exec() 


if __name__ == "__main__":
    main()


# TODO 
# 
# 
# *** done *** copy cells from Table on double click. remove edit_entry from double click.
# 
# *** done ***  view password toggle in EntryDialog
# *** done ***  status bar at bottom of window
#  *** done *** password generator in EntryDialog
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
