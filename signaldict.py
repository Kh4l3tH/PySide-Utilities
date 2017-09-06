from PySide import QtCore


class SignalDict(QtCore.QObject):
    changed = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.dict = dict()

    def __getitem__(self, key):
        return self.dict.__getitem__(key)

    def __iter__(self):
        return self.dict.__iter__()

    def __len__(self):
        return self.dict.__len__()

    def __setitem__(self, key, value):
        self.dict.__setitem__(key, value)
        self.changed.emit()

    def __str__(self):
        return self.dict.__str__()

    def items(self):
        return self.dict.items()

    def keys(self):
        return self.dict.keys()

    def pop(self, key):
        value = self.dict.pop(key)
        self.changed.emit()
        return value

    def setdefault(self, key, default=None):
        self.dict.setdefault(key, default)
        self.changed.emit()

    def values(self):
        return self.dict.values()
