from PySide import QtCore


class SignalDict(QtCore.QObject):
    changed = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.dict = dict()

    def __len__(self):
        return self.dict.__len__()

    def __setitem__(self, key, value):
        self.dict.__setitem__(key, value)
        self.changed.emit()
