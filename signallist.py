from PySide import QtCore


class SignalList(QtCore.QObject):
    changed = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.list = list()

    def append(self, x):
        self.list.append(x)
        self.changed.emit()
