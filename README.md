# PySide-Utilities
Some utilities that make working with PySide easier

## SignalList
The purpose of a SignalList is to mimic the behaviour of a python list while signalling changes

## SignalListModel
Using a SignalList as a source, a SignalListModel ensures that a QListView always shows the latest data of a list

## SignalDict
The purpose of a SignalDict is to mimic the behaviour of a python dict while signalling changes

## SignalDictModel
Using a SignalDict as a source, a SignalDictModel ensures that a QListView always shows the latest data of a dict.
It delivers the keys of the dict for Qt.DisplayRole and the values of the dict for Qt.UserRole

## FileSystemWatcher
Watches for file changes in a single folder. Supports adding/removing/modifying files.

###### Usage:
    watcher = filesystemwatcher.FileSystemWatcher(self.target)
    watcher.fileAdded.connect(function)
    watcher.fileRemoved.connect(function)
    watcher.fileModified.connect(function)

###### Example:
See `examples/folder_observer`

**Note: ** This implementation is not recursive and doesn't support folders yet
