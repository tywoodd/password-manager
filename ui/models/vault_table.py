from PySide6.QtCore import Qt, QAbstractTableModel


class VaultTableModel(QAbstractTableModel):
    def __init__(self, entries, parent=None):
        super().__init__(parent)
        self._entries = entries
        self._headers = ["UUID", "Title", "Username", "Password", "URL", "Notes"]


    def rowCount(self, parent=None):
        return len(self._entries)


    def columnCount(self, parent=None):
        return len(self._headers)


    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        
        if role == Qt.DisplayRole:
            entry = self._entries[index.row()]
            if index.column() == 0:
                return entry["uuid"]  
            elif index.column() == 1:
                return entry["title"]
            elif index.column() == 2:
                return entry["username"]
            elif index.column() == 3:
                return "*****"
            elif index.column() == 4:
                return entry["url"]         
            elif index.column() == 5:
                return entry["notes"]  

        return None
    
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return super().headerData(section, orientation, role)