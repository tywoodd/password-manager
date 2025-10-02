import json
from core.db import init_db, SessionLocal
from getpass import getpass
from core.vault import get_or_create_policy, derive_kek, get_or_create_active_key_ref, unwrap_dek, write_entry, read_entry
from core.models import VaultData
from ui.main_window import MainWindow
from ui.models.vault_table import VaultTableModel
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
import sys


# Pull UUIDs from DB, decrypt each entry, and build a list
def load_entries(session, vault):

    uuids = [u for (u,) in session.query(VaultData.entry_uuid)
                                .order_by(VaultData.id.desc()).all()]
    items = []
    for entry_uuid in uuids:
        data = read_entry(session=session, vault=vault, entry_uuid=entry_uuid)
        items.append({
            "uuid": entry_uuid,
            "title": data.get("title", ""),
            "username": data.get("username", ""),
            "password": data.get("password", ""),
            "url": data.get("url", ""),
            "notes": data.get("notes", "")
        })
    return items


def main():
    # DB + Policy boostrap
    init_db()
    session = SessionLocal()
    policy = get_or_create_policy(session)

    # Show App
    app = QApplication(sys.argv)
    window = MainWindow(app)


    def unlock_vault():
        master_password = window.passwordEdit.text().strip()

        # Derive KEK using master_password and kdf_policies
        # master_password = getpass("Enter master password: ")
        kek = derive_kek(master_password=master_password, policy=policy)
        del master_password

        # Obtain unwrapped DEK to write and read vault_data 
        key_ref = get_or_create_active_key_ref(session=session, kek=kek, policy=policy)    
        
        try:
            vault = unwrap_dek(session=session, key_ref=key_ref, kek=kek, policy=policy)  

        except Exception as e:
            window.unlockHintLabel.setText("Incorrect Password")
            QTimer.singleShot(3000, lambda: window.unlockHintLabel.setText(""))

        else:
            entries = load_entries(session=session, vault=vault)
            model = VaultTableModel(entries)
            window.table.setModel(model)

            window.unlock_vault()

            print(vault)
            entry = write_entry(
                session=session, 
                vault=vault, 
                title=input("Title: "), 
                username=input("Username: "), 
                password=getpass("Password: "), 
                url=input("URL: "), 
                notes=input("Notes: ")
            )
            print(entry)
            del vault
            


    window.unlockButton.clicked.connect(unlock_vault)
    window.passwordEdit.returnPressed.connect(unlock_vault)




    window.show()    
    app.exec() 

    # master_password = getpass("Enter master password: ")
    # kek = derive_kek(master_password=master_password, policy=policy)
    # del master_password

    # # Obtain unwrapped DEK to write and read vault_data 
    # key_ref = get_or_create_active_key_ref(session=session, kek=kek, policy=policy)    
    # vault = unwrap_dek(session=session, key_ref=key_ref, kek=kek, policy=policy)   

    # entry_to_read = read_entry(session=session, vault=vault, entry_uuid=entry)

    # print(json.dumps(entry_to_read, indent=4))


if __name__ == "__main__":
    main()


# TODO 
# 
# !!! TEST EVERYTHING !!!
# .
# 
# display entries in the table after unlocking vault
# 
# 
# 
# 
# 
# 
# 
# 
# .
