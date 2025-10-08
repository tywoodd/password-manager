from core.db import init_db, SessionLocal
from core.vault_service import VaultService
from ui.main_window import MainWindow
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

    window.unlockButton.clicked.connect(window.unlock_vault)
    window.passwordEdit.returnPressed.connect(window.unlock_vault)

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
#
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
