from PySide import QtCore
import os


class FileSystemWatcher(QtCore.QFileSystemWatcher):
    fileAdded = QtCore.Signal(str)
    fileRemoved = QtCore.Signal(str)
    fileModified = QtCore.Signal(str)

    def __init__(self, directory):
        self.root = os.path.abspath(directory)
        super().__init__([self.root])
        self.directoryChanged.connect(self.updatePaths)
        self.fileChanged.connect(self.checkFileModified)
        self.updatePaths()

    def checkFileModified(self, file):
        if file in self.files():
            self.fileModified.emit(file)

    def updatePaths(self):
        files = [os.path.join(self.root, file) for file in next(os.walk(self.root))[2]]
        for file in [file for file in self.files() if file not in files]:
            self.removePath(file)
            self.fileRemoved.emit(file)
        for file in [file for file in files if file not in self.files()]:
            self.addPath(file)
            self.fileAdded.emit(file)
