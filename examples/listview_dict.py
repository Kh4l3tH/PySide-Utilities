from PySide import QtCore
from PySide import QtGui
import random
import sys
import os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
import signaldictmodel
import signaldict


class Example(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

        self.dict = signaldict.SignalDict(a='1', b='2', c='3')
        self.model = signaldictmodel.SignalDictModel(self.dict)
        self.listview.setModel(self.model)
        selectionModel = self.listview.selectionModel()
        selectionModel.selectionChanged.connect(self.displaySelected)

        self.button.clicked.connect(self.addToDict)

    def displaySelected(self, item):
        modelindex = item.indexes()[0]
        data = self.model.data(modelindex, role=QtCore.Qt.UserRole)
        self.label.setText(data)

    def addToDict(self):
        num = random.random()
        self.dict[num] = str(num*2)

    def setupUi(self):
        self.button = QtGui.QPushButton('Add random data to dict')
        self.listview = QtGui.QListView()
        self.label = QtGui.QLabel('Selected value')

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.listview)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)


def main():
    app = QtGui.QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
