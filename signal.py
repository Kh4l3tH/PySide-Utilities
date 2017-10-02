class Signal():
    def __init__(self):
        self.receivers = []

    def connect(self, receiver):
        self.receivers.append(receiver)

    def emit(self):
        for receiver in self.receivers:
            receiver()
