import PySide2.QtCore as QtC


class DaemonWorker(QtC.QObject):
    sendText = QtC.Signal(str, int, int)
    sendText2DaemonWidget = QtC.Signal(str)

    def __init__(self, daemonWidget=None, parent=None):
        super(DaemonWorker, self).__init__(parent=parent)
        self.daemonWidget = daemonWidget