import PySide2.QtWidgets as QtW, PySide2.QtCore as QtC
from ui.mdiSubWidgets import Ui_Query_SubWidget


__all__ = ['Query_SubWidget']

class Query_SubWidget(QtW.QWidget, Ui_Query_SubWidget):
    def __init__(self, parent=None):
        super(Query_SubWidget, self).__init__(parent)
        self.setupUi(self)