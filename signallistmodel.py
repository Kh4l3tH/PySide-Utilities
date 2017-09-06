from PySide import QtCore


class SignalListModel(QtCore.QAbstractListModel):
    def __init__(self, list):
        super().__init__()
        self.list = list
        self.list.changed.connect(self.layoutChanged)

    def rowCount(self, parent):
        return len(self.list)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return self.list[index.row()]
