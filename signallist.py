from PySide import QtCore


class SignalList(QtCore.QObject):
    changed = QtCore.Signal()

    def __init__(self, iterable):
        super().__init__()
        self.list = list(iterable)

    def __getitem__(self, x):
        return self.list.__getitem__(x)

    def __len__(self):
        return self.list.__len__()

    def append(self, x):
        self.list.append(x)
        self.changed.emit()

    def extend(self, iterable):
        self.list.extend(iterable)
        self.changed.emit()

    def pop(self, index=-1):
        value = self.list.pop(index)
        self.changed.emit()
        return value
