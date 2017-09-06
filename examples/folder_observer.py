from PySide import QtGui
import sys
import os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
import filesystemwatcher


class Example(QtGui.QListWidget):
    def __init__(self):
        super().__init__()

        self.target = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test'))
        os.makedirs(self.target, exist_ok=True)

        self.obs = filesystemwatcher.FileSystemWatcher(self.target)
        self.obs.fileAdded.connect(lambda file: self.addItem(f'Added: {file}'))
        self.obs.fileRemoved.connect(lambda file: self.addItem(f'Removed: {file}'))
        self.obs.fileModified.connect(lambda file: self.addItem(f'Modified: {file}'))

    def showEvent(self, event):
        message = f'A folder has been created here:\n\n{self.target}\n\nAdd/Remove/Modify files (no folders) to this folder to receive corresponding Signals'
        QtGui.QMessageBox.information(None, None, message)
        return super().showEvent(event)


def main():
    app = QtGui.QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
