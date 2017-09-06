from PySide import QtGui
import random
import sys
import os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
import signallistmodel
import signallist


class Example(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

        self.list = signallist.SignalList()
        self.model = signallistmodel.SignalListModel(self.list)
        self.listview.setModel(self.model)

        self.button.clicked.connect(lambda: self.list.append(random.random()))

    def setupUi(self):
        self.button = QtGui.QPushButton('Add random number to list')
        self.listview = QtGui.QListView()

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.listview)
        layout.addWidget(self.button)
        self.setLayout(layout)


def main():
    app = QtGui.QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
