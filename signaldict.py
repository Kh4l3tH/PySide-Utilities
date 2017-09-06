from PySide import QtCore


class SignalDict(QtCore.QObject):
    changed = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.dict = dict()

    def __len__(self):
        return self.dict.__len__()
