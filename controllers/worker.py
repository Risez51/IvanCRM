from PyQt5 import QtCore


class Worker(QtCore.QObject):
    index_changed = QtCore.pyqtSignal(int)

    def run(self):
        for i in range(20):
            self.index_changed.emit(i)
            QtCore.QThread.msleep(1000)
