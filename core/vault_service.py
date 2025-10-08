from .vault import get_or_create_policy, derive_kek, get_or_create_active_key_ref, unwrap_dek, write_entry as _write_entry, read_entry as _read_entry, update_entry as _update_entry
from core.models import VaultData

class VaultService:

    def __init__(self, session):
        self._session = session
        self._dek = None
        self._unlocked = False

    def unlock(self, master_password) -> None:
        policy   = get_or_create_policy(self._session)
        kek      = derive_kek(master_password, policy)
        key_ref  = get_or_create_active_key_ref(session=self._session, kek=kek, policy=policy)
        self._dek = unwrap_dek(session=self._session, key_ref=key_ref, kek=kek, policy=policy)
        self._unlocked = True
        del master_password

    def lock(self) -> None:
        self._dek = None
        self._unlocked = False


    def is_unlocked(self) -> bool:
        return self._unlocked
    

    def write_entry(self, title, username, password, url, notes):
        assert self._unlocked and self._dek is not None, "Vault is locked."
        return _write_entry(
            session=self._session, 
            vault=self._dek, 
            title=title, 
            username=username, 
            password=password, 
            url=url, 
            notes=notes
        )

    def read_entry(self, entry_id: str) -> dict:
        assert self._unlocked and self._dek is not None, "Vault is locked."
        return _read_entry(self._session, self._dek, entry_id)
    

    def update_entry(self, entry_id: str, title, username, password, url, notes):
        assert self._unlocked and self._dek is not None, "Vault is locked."
        return _update_entry(
            session=self._session,
            vault=self._dek,
            entry_uuid=entry_id,
            title=title,
            username=username,
            password=password,
            url=url,
            notes=notes
        )
        

# ------- Get entries from the DB ------- Pull UUIDs from DB, decrypt each entry, and build a list of entries.

    def list_entries(self) -> list[dict]:

        uuids = [u for (u,) in self._session.query(VaultData.entry_uuid).order_by(VaultData.id.desc()).all()]
        items = []
        for entry_uuid in uuids:
            data = self.read_entry(entry_id=entry_uuid)
            items.append({
                "uuid": entry_uuid,
                "title": data.get("title", ""),
                "username": data.get("username", ""),
                "password": data.get("password", ""),
                "url": data.get("url", ""),
                "notes": data.get("notes", "")
            })
        return items