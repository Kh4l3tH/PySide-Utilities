import signal


class SignalList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.changed = Signal()

    def __delitem__(self, *args):
        super().__delitem__(*args)
        self.changed.emit()

    def __iadd__(self, *args):
        lst = super().__iadd__(*args)
        self.changed.emit()
        return lst

    def __imul__(self, *args):
        lst = super().__imul__(*args)
        self.changed.emit()
        return lst

    def __setitem__(self, *args):
        super().__setitem__(*args)
        self.changed.emit()

    def append(self, *args):
        super().append(*args)
        self.changed.emit()

    def clear(self):
        super().clear()
        self.changed.emit()

    def extend(self, *args):
        super().extend(*args)
        self.changed.emit()

    def insert(self, *args):
        super().insert(*args)
        self.changed.emit()

    def pop(self, *args):
        value = super().pop(*args)
        self.changed.emit()
        return value

    def remove(self, *args):
        super().remove(*args)
        self.changed.emit()

    def reverse(self):
        super().reverse()
        self.changed.emit()

    def sort(self, **kwargs):
        super().sort(**kwargs)
        self.changed.emit()
