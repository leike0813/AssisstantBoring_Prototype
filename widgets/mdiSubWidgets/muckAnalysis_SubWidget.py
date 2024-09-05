import PySide2.QtWidgets as QtW, PySide2.QtCore as QtC
from ui.mdiSubWidgets import Ui_MuckAnalysis_SubWidget


__all__ = ['MuckAnalysis_SubWidget']

class MuckAnalysis_SubWidget(QtW.QWidget, Ui_MuckAnalysis_SubWidget):
    def __init__(self, parent = None):
        super(MuckAnalysis_SubWidget, self).__init__(parent)
        self.setupUi(self)