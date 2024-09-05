import PySide2.QtWidgets as QtW, PySide2.QtCore as QtC
from ui.mdiSubWidgets import Ui_VibrationAnalysis_SubWidget


__all__ = ['VibrationAnalysis_SubWidget']

class VibrationAnalysis_SubWidget(QtW.QWidget, Ui_VibrationAnalysis_SubWidget):
    def __init__(self, parent=None):
        super(VibrationAnalysis_SubWidget, self).__init__(parent)
        self.setupUi(self)