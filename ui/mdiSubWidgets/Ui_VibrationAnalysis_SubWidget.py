# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_VibrationAnalysis_SubWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyside2_utils.widgets import QMatplotlibWidget


class Ui_VibrationAnalysis_SubWidget(object):
    def setupUi(self, VibrationAnalysis_SubWidget):
        if not VibrationAnalysis_SubWidget.objectName():
            VibrationAnalysis_SubWidget.setObjectName(u"VibrationAnalysis_SubWidget")
        VibrationAnalysis_SubWidget.resize(520, 520)
        self.verticalLayout = QVBoxLayout(VibrationAnalysis_SubWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.groupBox_14 = QGroupBox(VibrationAnalysis_SubWidget)
        self.groupBox_14.setObjectName(u"groupBox_14")
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_14.setFont(font)
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.groupBox_14)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_20.addWidget(self.label_47)

        self.dateEdit = QDateEdit(self.groupBox_14)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDateTime(QDateTime(QDate(2018, 6, 27), QTime(0, 0, 0)))

        self.verticalLayout_20.addWidget(self.dateEdit)

        self.label_48 = QLabel(self.groupBox_14)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_20.addWidget(self.label_48)

        self.time_ComboBox = QComboBox(self.groupBox_14)
        self.time_ComboBox.addItem("")
        self.time_ComboBox.setObjectName(u"time_ComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_ComboBox.sizePolicy().hasHeightForWidth())
        self.time_ComboBox.setSizePolicy(sizePolicy)
        self.time_ComboBox.setMaximumSize(QSize(16777215, 20))
        self.time_ComboBox.setFrame(True)

        self.verticalLayout_20.addWidget(self.time_ComboBox)


        self.horizontalLayout_13.addWidget(self.groupBox_14)

        self.groupBox_15 = QGroupBox(VibrationAnalysis_SubWidget)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setFont(font)
        self.gridLayout_10 = QGridLayout(self.groupBox_15)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pene_LineEdit = QLineEdit(self.groupBox_15)
        self.pene_LineEdit.setObjectName(u"pene_LineEdit")

        self.gridLayout_10.addWidget(self.pene_LineEdit, 1, 3, 1, 1)

        self.label_49 = QLabel(self.groupBox_15)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_10.addWidget(self.label_49, 0, 0, 1, 1)

        self.label_50 = QLabel(self.groupBox_15)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_10.addWidget(self.label_50, 1, 2, 1, 1)

        self.th_LineEdit = QLineEdit(self.groupBox_15)
        self.th_LineEdit.setObjectName(u"th_LineEdit")

        self.gridLayout_10.addWidget(self.th_LineEdit, 0, 1, 1, 1)

        self.label_51 = QLabel(self.groupBox_15)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_10.addWidget(self.label_51, 1, 0, 1, 1)

        self.rpm_LineEdit = QLineEdit(self.groupBox_15)
        self.rpm_LineEdit.setObjectName(u"rpm_LineEdit")

        self.gridLayout_10.addWidget(self.rpm_LineEdit, 0, 3, 1, 1)

        self.label_52 = QLabel(self.groupBox_15)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_10.addWidget(self.label_52, 0, 2, 1, 1)

        self.tor_LineEdit = QLineEdit(self.groupBox_15)
        self.tor_LineEdit.setObjectName(u"tor_LineEdit")

        self.gridLayout_10.addWidget(self.tor_LineEdit, 1, 1, 1, 1)

        self.label_53 = QLabel(self.groupBox_15)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_10.addWidget(self.label_53, 2, 0, 1, 1)

        self.spd_LineEdit = QLineEdit(self.groupBox_15)
        self.spd_LineEdit.setObjectName(u"spd_LineEdit")

        self.gridLayout_10.addWidget(self.spd_LineEdit, 2, 1, 1, 1)

        self.label_54 = QLabel(self.groupBox_15)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_10.addWidget(self.label_54, 2, 2, 1, 1)

        self.pressure_LineEdit = QLineEdit(self.groupBox_15)
        self.pressure_LineEdit.setObjectName(u"pressure_LineEdit")
        self.pressure_LineEdit.setEnabled(False)

        self.gridLayout_10.addWidget(self.pressure_LineEdit, 2, 3, 1, 1)


        self.horizontalLayout_13.addWidget(self.groupBox_15)

        self.horizontalLayout_13.setStretch(0, 3)
        self.horizontalLayout_13.setStretch(1, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.groupBox_16 = QGroupBox(VibrationAnalysis_SubWidget)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setFont(font)
        self.gridLayout_11 = QGridLayout(self.groupBox_16)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.historyCurve_MatplotlibWidget = QMatplotlibWidget(self.groupBox_16)
        self.historyCurve_MatplotlibWidget.setObjectName(u"historyCurve_MatplotlibWidget")

        self.gridLayout_11.addWidget(self.historyCurve_MatplotlibWidget, 0, 0, 1, 1)

        self.gridLayout_11.setRowStretch(0, 1)

        self.verticalLayout.addWidget(self.groupBox_16)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 0)
        self.groupBox_17 = QGroupBox(VibrationAnalysis_SubWidget)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setFont(font)
        self.gridLayout_12 = QGridLayout(self.groupBox_17)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.ppv_LineEdit = QLineEdit(self.groupBox_17)
        self.ppv_LineEdit.setObjectName(u"ppv_LineEdit")

        self.gridLayout_12.addWidget(self.ppv_LineEdit, 0, 1, 1, 1)

        self.label_55 = QLabel(self.groupBox_17)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_12.addWidget(self.label_55, 2, 0, 1, 1)

        self.va_LineEdit = QLineEdit(self.groupBox_17)
        self.va_LineEdit.setObjectName(u"va_LineEdit")

        self.gridLayout_12.addWidget(self.va_LineEdit, 3, 1, 1, 1)

        self.label_56 = QLabel(self.groupBox_17)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_12.addWidget(self.label_56, 0, 0, 1, 1)

        self.ve_LineEdit = QLineEdit(self.groupBox_17)
        self.ve_LineEdit.setObjectName(u"ve_LineEdit")

        self.gridLayout_12.addWidget(self.ve_LineEdit, 2, 1, 1, 1)

        self.label_57 = QLabel(self.groupBox_17)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_12.addWidget(self.label_57, 3, 0, 1, 1)

        self.label_58 = QLabel(self.groupBox_17)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_12.addWidget(self.label_58, 4, 0, 1, 1)

        self.rms_LineEdit = QLineEdit(self.groupBox_17)
        self.rms_LineEdit.setObjectName(u"rms_LineEdit")

        self.gridLayout_12.addWidget(self.rms_LineEdit, 4, 1, 1, 1)


        self.horizontalLayout_14.addWidget(self.groupBox_17)

        self.charasticCurve_MatplotlibWidget = QMatplotlibWidget(VibrationAnalysis_SubWidget)
        self.charasticCurve_MatplotlibWidget.setObjectName(u"charasticCurve_MatplotlibWidget")

        self.horizontalLayout_14.addWidget(self.charasticCurve_MatplotlibWidget)

        self.horizontalLayout_14.setStretch(0, 3)
        self.horizontalLayout_14.setStretch(1, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.groupBox_4 = QGroupBox(VibrationAnalysis_SubWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.filtedCurve_MatplotlibWidget = QMatplotlibWidget(self.groupBox_4)
        self.filtedCurve_MatplotlibWidget.setObjectName(u"filtedCurve_MatplotlibWidget")

        self.verticalLayout_12.addWidget(self.filtedCurve_MatplotlibWidget)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 3)

        self.retranslateUi(VibrationAnalysis_SubWidget)

        QMetaObject.connectSlotsByName(VibrationAnalysis_SubWidget)
    # setupUi

    def retranslateUi(self, VibrationAnalysis_SubWidget):
        VibrationAnalysis_SubWidget.setWindowTitle(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u5200\u76d8\u632f\u52a8\u5206\u6790", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u91c7\u6837\u65f6\u95f4\u9009\u62e9", None))
        self.label_47.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u65e5\u671f", None))
        self.label_48.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u91c7\u6837\u65f6\u95f4", None))
        self.time_ComboBox.setItemText(0, QCoreApplication.translate("VibrationAnalysis_SubWidget", u"00:02:00", None))

        self.groupBox_15.setTitle(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u5b9e\u65f6\u6398\u8fdb\u53c2\u6570", None))
        self.pene_LineEdit.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"6.41  mm", None))
        self.label_49.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u603b\u63a8\u529b", None))
        self.label_50.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u8d2f\u5165\u5ea6", None))
        self.th_LineEdit.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"10358.5  kN", None))
        self.label_51.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u5200\u76d8\u626d\u77e9", None))
        self.rpm_LineEdit.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"6.1", None))
        self.label_52.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u5200\u76d8\u8f6c\u901f", None))
        self.tor_LineEdit.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"1661.77  kN\u00b7m", None))
        self.label_53.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u63a8\u8fdb\u901f\u5ea6", None))
        self.spd_LineEdit.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"39.42  mm/min", None))
        self.label_54.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u76ae\u5e26\u673a\u538b\u529b", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u632f\u52a8\u65f6\u7a0b\u66f2\u7ebf", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u632f\u52a8\u7279\u5f81", None))
        self.ppv_LineEdit.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"15.8", None))
        self.label_55.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"Ve", None))
        self.va_LineEdit.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"1.03", None))
        self.label_56.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"PPV", None))
        self.ve_LineEdit.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"2.41", None))
        self.label_57.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"Va", None))
        self.label_58.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"RMS", None))
        self.rms_LineEdit.setText(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"352", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("VibrationAnalysis_SubWidget", u"\u6ee4\u6ce2\u540e\u66f2\u7ebf(Z)", None))
    # retranslateUi

