import signal


class SignalDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.changed = signal.Signal()

    def __delitem__(self, *args):
        super().__delitem__(*args)
        self.changed.emit()

    def __setitem__(self, *args):
        super().__setitem__(*args)
        self.changed.emit()

    def clear(self):
        super().clear()
        self.changed.emit()

    def pop(self, *args):
        value = super().pop(*args)
        self.changed.emit()
        return value

    def popitem(self):
        value = super().popitem()
        self.changed.emit()
        return value

    def setdefault(self, *args):
        super().setdefault(*args)
        self.changed.emit()

    def update(self, *args):
        super().update(*args)
        self.changed.emit()
