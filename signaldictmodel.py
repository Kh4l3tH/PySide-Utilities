from PySide import QtCore


class SignalDictModel(QtCore.QAbstractListModel):
    def __init__(self, dict):
        super().__init__()
        self.dict = dict
        self.dict.changed.connect(self.layoutChanged.emit)

    def rowCount(self, parent):
        return len(self.dict)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return list(self.dict.keys())[index.row()]
        elif role == QtCore.Qt.UserRole:
            return list(self.dict.values())[index.row()]
