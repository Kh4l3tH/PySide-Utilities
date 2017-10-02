import collections
import signal


class OrderedSignalDict(collections.OrderedDict):
    def __init__(self, *args, **kwargs):
        self.changed = signal.Signal()
        super().__init__(*args, **kwargs)

    def __delitem__(self, *args):
        super().__delitem__(*args)
        self.changed.emit()

    def __setitem__(self, *args):
        super().__setitem__(*args)
        self.changed.emit()

    def clear(self):
        super().clear()
        self.changed.emit()

    def move_to_end(self, *args):
        super().move_to_end(*args)
        self.changed.emit()

    def pop(self, *args):
        value = super().pop(*args)
        self.changed.emit()
        return value

    def popitem(self, *args):
        value = super().popitem(*args)
        self.changed.emit()
        return value

    def setdefault(self, *args):
        super().setdefault(*args)
        self.changed.emit()

    def sort(self, key=None, reverse=False):
        tmp = sorted(list(self.items()), key=lambda x: key(x[0], x[1]), reverse=reverse)
        super().clear()
        for k, v in tmp:
            super().__setitem__(k, v)
        self.changed.emit()

    def update(self, *args):
        super().update(*args)
        self.changed.emit()
