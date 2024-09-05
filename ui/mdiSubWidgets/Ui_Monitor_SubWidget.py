# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Monitor_SubWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyside2_utils.widgets import QDynamicSeriesPlotWidget


class Ui_Monitor_SubWidget(object):
    def setupUi(self, Monitor_SubWidget):
        if not Monitor_SubWidget.objectName():
            Monitor_SubWidget.setObjectName(u"Monitor_SubWidget")
        Monitor_SubWidget.resize(1920, 1080)
        self.verticalLayout_2 = QVBoxLayout(Monitor_SubWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.muckImage_GroupBox = QGroupBox(Monitor_SubWidget)
        self.muckImage_GroupBox.setObjectName(u"muckImage_GroupBox")
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.muckImage_GroupBox.setFont(font)
        self.verticalLayout_7 = QVBoxLayout(self.muckImage_GroupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(6, 12, 6, 6)
        self.muckImage_Label = QLabel(self.muckImage_GroupBox)
        self.muckImage_Label.setObjectName(u"muckImage_Label")

        self.verticalLayout_7.addWidget(self.muckImage_Label)


        self.horizontalLayout_2.addWidget(self.muckImage_GroupBox)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_33 = QLabel(Monitor_SubWidget)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_5.addWidget(self.label_33)

        self.label_12 = QLabel(Monitor_SubWidget)
        self.label_12.setObjectName(u"label_12")
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_12)

        self.vol_LCD = QLCDNumber(Monitor_SubWidget)
        self.vol_LCD.setObjectName(u"vol_LCD")
        self.vol_LCD.setSmallDecimalPoint(True)
        self.vol_LCD.setDigitCount(5)

        self.verticalLayout_5.addWidget(self.vol_LCD)

        self.label_24 = QLabel(Monitor_SubWidget)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_5.addWidget(self.label_24)

        self.label_25 = QLabel(Monitor_SubWidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_25)

        self.d50_LCD = QLCDNumber(Monitor_SubWidget)
        self.d50_LCD.setObjectName(u"d50_LCD")
        self.d50_LCD.setSmallDecimalPoint(True)
        self.d50_LCD.setDigitCount(5)

        self.verticalLayout_5.addWidget(self.d50_LCD)

        self.label_26 = QLabel(Monitor_SubWidget)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_5.addWidget(self.label_26)

        self.label_27 = QLabel(Monitor_SubWidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_27)

        self.cu_LCD = QLCDNumber(Monitor_SubWidget)
        self.cu_LCD.setObjectName(u"cu_LCD")
        self.cu_LCD.setSmallDecimalPoint(True)
        self.cu_LCD.setDigitCount(5)

        self.verticalLayout_5.addWidget(self.cu_LCD)

        self.label_28 = QLabel(Monitor_SubWidget)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_5.addWidget(self.label_28)

        self.label_29 = QLabel(Monitor_SubWidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_29)

        self.cc_LCD = QLCDNumber(Monitor_SubWidget)
        self.cc_LCD.setObjectName(u"cc_LCD")
        self.cc_LCD.setSmallDecimalPoint(True)
        self.cc_LCD.setDigitCount(5)

        self.verticalLayout_5.addWidget(self.cc_LCD)

        self.label_30 = QLabel(Monitor_SubWidget)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_5.addWidget(self.label_30)

        self.label_31 = QLabel(Monitor_SubWidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_31)

        self.ci_LCD = QLCDNumber(Monitor_SubWidget)
        self.ci_LCD.setObjectName(u"ci_LCD")
        self.ci_LCD.setSmallDecimalPoint(True)
        self.ci_LCD.setDigitCount(5)

        self.verticalLayout_5.addWidget(self.ci_LCD)

        self.label_34 = QLabel(Monitor_SubWidget)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_5.addWidget(self.label_34)

        self.verticalLayout_5.setStretch(0, 14)
        self.verticalLayout_5.setStretch(1, 8)
        self.verticalLayout_5.setStretch(2, 8)
        self.verticalLayout_5.setStretch(3, 1)
        self.verticalLayout_5.setStretch(4, 8)
        self.verticalLayout_5.setStretch(5, 8)
        self.verticalLayout_5.setStretch(6, 1)
        self.verticalLayout_5.setStretch(7, 8)
        self.verticalLayout_5.setStretch(8, 8)
        self.verticalLayout_5.setStretch(9, 1)
        self.verticalLayout_5.setStretch(10, 8)
        self.verticalLayout_5.setStretch(11, 8)
        self.verticalLayout_5.setStretch(12, 1)
        self.verticalLayout_5.setStretch(13, 8)
        self.verticalLayout_5.setStretch(14, 8)
        self.verticalLayout_5.setStretch(15, 14)

        self.horizontalLayout_8.addLayout(self.verticalLayout_5)

        self.muckParameter_Curve_Widget = QDynamicSeriesPlotWidget(Monitor_SubWidget)
        self.muckParameter_Curve_Widget.setObjectName(u"muckParameter_Curve_Widget")

        self.horizontalLayout_8.addWidget(self.muckParameter_Curve_Widget)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 8)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(Monitor_SubWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_11 = QLabel(Monitor_SubWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_11)

        self.pr_LCD = QLCDNumber(Monitor_SubWidget)
        self.pr_LCD.setObjectName(u"pr_LCD")
        self.pr_LCD.setSmallDecimalPoint(True)
        self.pr_LCD.setDigitCount(5)

        self.verticalLayout_4.addWidget(self.pr_LCD)

        self.label_17 = QLabel(Monitor_SubWidget)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_4.addWidget(self.label_17)

        self.label_13 = QLabel(Monitor_SubWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_13)

        self.f_LCD = QLCDNumber(Monitor_SubWidget)
        self.f_LCD.setObjectName(u"f_LCD")
        self.f_LCD.setSmallDecimalPoint(True)
        self.f_LCD.setDigitCount(5)

        self.verticalLayout_4.addWidget(self.f_LCD)

        self.label_18 = QLabel(Monitor_SubWidget)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_4.addWidget(self.label_18)

        self.label_14 = QLabel(Monitor_SubWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_14)

        self.vr_LCD = QLCDNumber(Monitor_SubWidget)
        self.vr_LCD.setObjectName(u"vr_LCD")
        self.vr_LCD.setSmallDecimalPoint(True)
        self.vr_LCD.setDigitCount(5)

        self.verticalLayout_4.addWidget(self.vr_LCD)

        self.label_19 = QLabel(Monitor_SubWidget)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_4.addWidget(self.label_19)

        self.label_15 = QLabel(Monitor_SubWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_15)

        self.t_LCD = QLCDNumber(Monitor_SubWidget)
        self.t_LCD.setObjectName(u"t_LCD")
        self.t_LCD.setSmallDecimalPoint(True)
        self.t_LCD.setDigitCount(5)

        self.verticalLayout_4.addWidget(self.t_LCD)

        self.label_20 = QLabel(Monitor_SubWidget)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_4.addWidget(self.label_20)

        self.label_16 = QLabel(Monitor_SubWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_16)

        self.vp_LCD = QLCDNumber(Monitor_SubWidget)
        self.vp_LCD.setObjectName(u"vp_LCD")
        self.vp_LCD.setSmallDecimalPoint(True)
        self.vp_LCD.setDigitCount(5)

        self.verticalLayout_4.addWidget(self.vp_LCD)

        self.label_10 = QLabel(Monitor_SubWidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.verticalLayout_4.setStretch(0, 14)
        self.verticalLayout_4.setStretch(1, 8)
        self.verticalLayout_4.setStretch(2, 8)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 8)
        self.verticalLayout_4.setStretch(5, 8)
        self.verticalLayout_4.setStretch(6, 1)
        self.verticalLayout_4.setStretch(7, 8)
        self.verticalLayout_4.setStretch(8, 8)
        self.verticalLayout_4.setStretch(9, 1)
        self.verticalLayout_4.setStretch(10, 8)
        self.verticalLayout_4.setStretch(11, 8)
        self.verticalLayout_4.setStretch(12, 1)
        self.verticalLayout_4.setStretch(13, 8)
        self.verticalLayout_4.setStretch(14, 8)
        self.verticalLayout_4.setStretch(15, 14)

        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.boringParameter_Curve_Widget = QDynamicSeriesPlotWidget(Monitor_SubWidget)
        self.boringParameter_Curve_Widget.setObjectName(u"boringParameter_Curve_Widget")

        self.horizontalLayout_7.addWidget(self.boringParameter_Curve_Widget)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 8)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.rock_Curve_GroupBox = QGroupBox(Monitor_SubWidget)
        self.rock_Curve_GroupBox.setObjectName(u"rock_Curve_GroupBox")
        self.rock_Curve_GroupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.rock_Curve_GroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rockInformation_Curve_Widget = QDynamicSeriesPlotWidget(self.rock_Curve_GroupBox)
        self.rockInformation_Curve_Widget.setObjectName(u"rockInformation_Curve_Widget")

        self.verticalLayout.addWidget(self.rockInformation_Curve_Widget)


        self.verticalLayout_3.addWidget(self.rock_Curve_GroupBox)

        self.verticalLayout_3.setStretch(0, 7)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.v_layout_center = QVBoxLayout()
        self.v_layout_center.setSpacing(10)
        self.v_layout_center.setObjectName(u"v_layout_center")
        self.basicInfo_GroupBox = QGroupBox(Monitor_SubWidget)
        self.basicInfo_GroupBox.setObjectName(u"basicInfo_GroupBox")
        self.basicInfo_GroupBox.setFont(font)
        self.formLayout = QFormLayout(self.basicInfo_GroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setVerticalSpacing(3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.basicInfo_GroupBox)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"Microsoft YaHei UI")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.label.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.dateTimeEdit = QDateTimeEdit(self.basicInfo_GroupBox)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        font3 = QFont()
        font3.setFamily(u"Microsoft YaHei UI")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.dateTimeEdit.setFont(font3)
        self.dateTimeEdit.setAlignment(Qt.AlignCenter)
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setDate(QDate(2018, 6, 27))
        self.dateTimeEdit.setTime(QTime(0, 22, 59))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateTimeEdit)

        self.label_2 = QLabel(self.basicInfo_GroupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.mileage_LineEdit = QLineEdit(self.basicInfo_GroupBox)
        self.mileage_LineEdit.setObjectName(u"mileage_LineEdit")
        self.mileage_LineEdit.setFont(font3)
        self.mileage_LineEdit.setAlignment(Qt.AlignCenter)
        self.mileage_LineEdit.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.mileage_LineEdit)

        self.label_5 = QLabel(self.basicInfo_GroupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.status_LineEdit = QLineEdit(self.basicInfo_GroupBox)
        self.status_LineEdit.setObjectName(u"status_LineEdit")
        self.status_LineEdit.setFont(font)
        self.status_LineEdit.setAlignment(Qt.AlignCenter)
        self.status_LineEdit.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.status_LineEdit)


        self.v_layout_center.addWidget(self.basicInfo_GroupBox)

        self.rockCondition_GroupBox = QGroupBox(Monitor_SubWidget)
        self.rockCondition_GroupBox.setObjectName(u"rockCondition_GroupBox")
        self.rockCondition_GroupBox.setFont(font)
        self.gridLayout_2 = QGridLayout(self.rockCondition_GroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.rockGrade_LineEdit = QLineEdit(self.rockCondition_GroupBox)
        self.rockGrade_LineEdit.setObjectName(u"rockGrade_LineEdit")
        font4 = QFont()
        font4.setFamily(u"Microsoft YaHei UI")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.rockGrade_LineEdit.setFont(font4)
        self.rockGrade_LineEdit.setAlignment(Qt.AlignCenter)
        self.rockGrade_LineEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.rockGrade_LineEdit, 2, 2, 1, 1)

        self.ucs_LineEdit = QLineEdit(self.rockCondition_GroupBox)
        self.ucs_LineEdit.setObjectName(u"ucs_LineEdit")
        self.ucs_LineEdit.setFont(font4)
        self.ucs_LineEdit.setAlignment(Qt.AlignCenter)
        self.ucs_LineEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.ucs_LineEdit, 2, 4, 1, 1)

        self.label_6 = QLabel(self.rockCondition_GroupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout_2.addWidget(self.label_6, 2, 5, 1, 1)

        self.label_3 = QLabel(self.rockCondition_GroupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.kv_LineEdit = QLineEdit(self.rockCondition_GroupBox)
        self.kv_LineEdit.setObjectName(u"kv_LineEdit")
        self.kv_LineEdit.setFont(font4)
        self.kv_LineEdit.setAlignment(Qt.AlignCenter)
        self.kv_LineEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.kv_LineEdit, 2, 6, 1, 1)

        self.label_4 = QLabel(self.rockCondition_GroupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout_2.addWidget(self.label_4, 2, 3, 1, 1)


        self.v_layout_center.addWidget(self.rockCondition_GroupBox)

        self.suggestion_GroupBox = QGroupBox(Monitor_SubWidget)
        self.suggestion_GroupBox.setObjectName(u"suggestion_GroupBox")
        self.suggestion_GroupBox.setFont(font)
        self.verticalLayout_8 = QVBoxLayout(self.suggestion_GroupBox)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.suggestParameter_GridLayout = QGridLayout()
        self.suggestParameter_GridLayout.setObjectName(u"suggestParameter_GridLayout")
        self.suggestParameter_GridLayout.setVerticalSpacing(6)
        self.suggestParameter_GridLayout.setContentsMargins(-1, -1, -1, 0)
        self.suggest_f_PerfMode_LineEdit = QLineEdit(self.suggestion_GroupBox)
        self.suggest_f_PerfMode_LineEdit.setObjectName(u"suggest_f_PerfMode_LineEdit")
        self.suggest_f_PerfMode_LineEdit.setFont(font)
        self.suggest_f_PerfMode_LineEdit.setAlignment(Qt.AlignCenter)
        self.suggest_f_PerfMode_LineEdit.setReadOnly(True)

        self.suggestParameter_GridLayout.addWidget(self.suggest_f_PerfMode_LineEdit, 1, 1, 1, 1)

        self.suggest_vr_PerfMode_LineEdit = QLineEdit(self.suggestion_GroupBox)
        self.suggest_vr_PerfMode_LineEdit.setObjectName(u"suggest_vr_PerfMode_LineEdit")
        self.suggest_vr_PerfMode_LineEdit.setFont(font)
        self.suggest_vr_PerfMode_LineEdit.setAlignment(Qt.AlignCenter)
        self.suggest_vr_PerfMode_LineEdit.setReadOnly(True)

        self.suggestParameter_GridLayout.addWidget(self.suggest_vr_PerfMode_LineEdit, 2, 1, 1, 1)

        self.label_22 = QLabel(self.suggestion_GroupBox)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)

        self.suggestParameter_GridLayout.addWidget(self.label_22, 1, 0, 1, 1)

        self.suggest_f_EcoMode_LineEdit = QLineEdit(self.suggestion_GroupBox)
        self.suggest_f_EcoMode_LineEdit.setObjectName(u"suggest_f_EcoMode_LineEdit")
        self.suggest_f_EcoMode_LineEdit.setFont(font)
        self.suggest_f_EcoMode_LineEdit.setAlignment(Qt.AlignCenter)
        self.suggest_f_EcoMode_LineEdit.setReadOnly(True)

        self.suggestParameter_GridLayout.addWidget(self.suggest_f_EcoMode_LineEdit, 1, 2, 1, 1)

        self.label_92 = QLabel(self.suggestion_GroupBox)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font)
        self.label_92.setAlignment(Qt.AlignCenter)

        self.suggestParameter_GridLayout.addWidget(self.label_92, 0, 2, 1, 1)

        self.label_93 = QLabel(self.suggestion_GroupBox)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font)

        self.suggestParameter_GridLayout.addWidget(self.label_93, 1, 3, 1, 1)

        self.label_23 = QLabel(self.suggestion_GroupBox)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)

        self.suggestParameter_GridLayout.addWidget(self.label_23, 2, 0, 1, 1)

        self.suggest_vr_EcoMode_LineEdit = QLineEdit(self.suggestion_GroupBox)
        self.suggest_vr_EcoMode_LineEdit.setObjectName(u"suggest_vr_EcoMode_LineEdit")
        self.suggest_vr_EcoMode_LineEdit.setFont(font)
        self.suggest_vr_EcoMode_LineEdit.setAlignment(Qt.AlignCenter)
        self.suggest_vr_EcoMode_LineEdit.setReadOnly(True)

        self.suggestParameter_GridLayout.addWidget(self.suggest_vr_EcoMode_LineEdit, 2, 2, 1, 1)

        self.label_90 = QLabel(self.suggestion_GroupBox)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font)
        self.label_90.setAlignment(Qt.AlignCenter)

        self.suggestParameter_GridLayout.addWidget(self.label_90, 0, 1, 1, 1)

        self.label_94 = QLabel(self.suggestion_GroupBox)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font)

        self.suggestParameter_GridLayout.addWidget(self.label_94, 2, 3, 1, 1)

        self.suggestParameter_GridLayout.setRowStretch(1, 1)
        self.suggestParameter_GridLayout.setRowStretch(2, 1)

        self.verticalLayout_8.addLayout(self.suggestParameter_GridLayout)


        self.v_layout_center.addWidget(self.suggestion_GroupBox)

        self.v_layout_center.setStretch(0, 2)
        self.v_layout_center.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.v_layout_center)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.support_GroupBox = QGroupBox(Monitor_SubWidget)
        self.support_GroupBox.setObjectName(u"support_GroupBox")
        self.support_GroupBox.setFont(font)
        self.verticalLayout_34 = QVBoxLayout(self.support_GroupBox)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.bolt_GridLayout = QGridLayout()
        self.bolt_GridLayout.setObjectName(u"bolt_GridLayout")
        self.bolt_GridLayout.setVerticalSpacing(0)
        self.bolt_GridLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_77 = QLabel(self.support_GroupBox)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font3)

        self.bolt_GridLayout.addWidget(self.label_77, 1, 0, 1, 1)

        self.boltLength_LineEdit = QLineEdit(self.support_GroupBox)
        self.boltLength_LineEdit.setObjectName(u"boltLength_LineEdit")
        self.boltLength_LineEdit.setFont(font3)
        self.boltLength_LineEdit.setReadOnly(True)

        self.bolt_GridLayout.addWidget(self.boltLength_LineEdit, 0, 3, 1, 1)

        self.label_73 = QLabel(self.support_GroupBox)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font3)

        self.bolt_GridLayout.addWidget(self.label_73, 0, 2, 1, 1)

        self.boltModel_LineEdit = QLineEdit(self.support_GroupBox)
        self.boltModel_LineEdit.setObjectName(u"boltModel_LineEdit")
        self.boltModel_LineEdit.setFont(font3)
        self.boltModel_LineEdit.setReadOnly(True)

        self.bolt_GridLayout.addWidget(self.boltModel_LineEdit, 0, 1, 1, 1)

        self.boltLongiSpacing_LineEdit = QLineEdit(self.support_GroupBox)
        self.boltLongiSpacing_LineEdit.setObjectName(u"boltLongiSpacing_LineEdit")
        self.boltLongiSpacing_LineEdit.setFont(font3)
        self.boltLongiSpacing_LineEdit.setReadOnly(True)

        self.bolt_GridLayout.addWidget(self.boltLongiSpacing_LineEdit, 1, 3, 1, 1)

        self.boltHoopSpacing_LineEdit = QLineEdit(self.support_GroupBox)
        self.boltHoopSpacing_LineEdit.setObjectName(u"boltHoopSpacing_LineEdit")
        self.boltHoopSpacing_LineEdit.setFont(font3)
        self.boltHoopSpacing_LineEdit.setReadOnly(True)

        self.bolt_GridLayout.addWidget(self.boltHoopSpacing_LineEdit, 1, 1, 1, 1)

        self.label_78 = QLabel(self.support_GroupBox)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font3)

        self.bolt_GridLayout.addWidget(self.label_78, 1, 2, 1, 1)

        self.label_72 = QLabel(self.support_GroupBox)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font3)

        self.bolt_GridLayout.addWidget(self.label_72, 0, 0, 1, 1)

        self.label_79 = QLabel(self.support_GroupBox)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font3)

        self.bolt_GridLayout.addWidget(self.label_79, 2, 0, 1, 1)

        self.boltRange_LineEdit = QLineEdit(self.support_GroupBox)
        self.boltRange_LineEdit.setObjectName(u"boltRange_LineEdit")
        self.boltRange_LineEdit.setFont(font3)
        self.boltRange_LineEdit.setReadOnly(True)

        self.bolt_GridLayout.addWidget(self.boltRange_LineEdit, 2, 1, 1, 1)

        self.bolt_GridLayout.setColumnStretch(0, 4)
        self.bolt_GridLayout.setColumnStretch(1, 5)
        self.bolt_GridLayout.setColumnStretch(2, 4)
        self.bolt_GridLayout.setColumnStretch(3, 5)

        self.verticalLayout_34.addLayout(self.bolt_GridLayout)

        self.line = QFrame(self.support_GroupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.line)

        self.arch_GridLayout = QGridLayout()
        self.arch_GridLayout.setObjectName(u"arch_GridLayout")
        self.arch_GridLayout.setVerticalSpacing(0)
        self.arch_GridLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_75 = QLabel(self.support_GroupBox)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font3)

        self.arch_GridLayout.addWidget(self.label_75, 0, 0, 1, 1)

        self.archModel_LineEdit = QLineEdit(self.support_GroupBox)
        self.archModel_LineEdit.setObjectName(u"archModel_LineEdit")
        self.archModel_LineEdit.setFont(font3)
        self.archModel_LineEdit.setReadOnly(True)

        self.arch_GridLayout.addWidget(self.archModel_LineEdit, 0, 1, 1, 1)

        self.label_74 = QLabel(self.support_GroupBox)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font3)

        self.arch_GridLayout.addWidget(self.label_74, 0, 2, 1, 1)

        self.archSpacing_LineEdit = QLineEdit(self.support_GroupBox)
        self.archSpacing_LineEdit.setObjectName(u"archSpacing_LineEdit")
        self.archSpacing_LineEdit.setFont(font3)
        self.archSpacing_LineEdit.setReadOnly(True)

        self.arch_GridLayout.addWidget(self.archSpacing_LineEdit, 0, 3, 1, 1)

        self.arch_GridLayout.setColumnStretch(0, 4)
        self.arch_GridLayout.setColumnStretch(1, 5)
        self.arch_GridLayout.setColumnStretch(2, 4)
        self.arch_GridLayout.setColumnStretch(3, 5)

        self.verticalLayout_34.addLayout(self.arch_GridLayout)

        self.line_2 = QFrame(self.support_GroupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.line_2)

        self.shotcrete_GridLayout = QGridLayout()
        self.shotcrete_GridLayout.setObjectName(u"shotcrete_GridLayout")
        self.shotcrete_GridLayout.setVerticalSpacing(0)
        self.shotcrete_GridLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_85 = QLabel(self.support_GroupBox)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font3)

        self.shotcrete_GridLayout.addWidget(self.label_85, 0, 0, 1, 1)

        self.shotInTime_LineEdit = QLineEdit(self.support_GroupBox)
        self.shotInTime_LineEdit.setObjectName(u"shotInTime_LineEdit")
        self.shotInTime_LineEdit.setFont(font3)
        self.shotInTime_LineEdit.setReadOnly(True)

        self.shotcrete_GridLayout.addWidget(self.shotInTime_LineEdit, 2, 1, 1, 1)

        self.netRange_LineEdit = QLineEdit(self.support_GroupBox)
        self.netRange_LineEdit.setObjectName(u"netRange_LineEdit")
        self.netRange_LineEdit.setFont(font3)
        self.netRange_LineEdit.setReadOnly(True)

        self.shotcrete_GridLayout.addWidget(self.netRange_LineEdit, 0, 3, 1, 1)

        self.label_82 = QLabel(self.support_GroupBox)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font3)

        self.shotcrete_GridLayout.addWidget(self.label_82, 2, 0, 1, 1)

        self.netModel_LineEdit = QLineEdit(self.support_GroupBox)
        self.netModel_LineEdit.setObjectName(u"netModel_LineEdit")
        self.netModel_LineEdit.setFont(font3)
        self.netModel_LineEdit.setReadOnly(True)

        self.shotcrete_GridLayout.addWidget(self.netModel_LineEdit, 0, 1, 1, 1)

        self.label_76 = QLabel(self.support_GroupBox)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font3)

        self.shotcrete_GridLayout.addWidget(self.label_76, 0, 2, 1, 1)

        self.label_80 = QLabel(self.support_GroupBox)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font3)

        self.shotcrete_GridLayout.addWidget(self.label_80, 1, 0, 1, 1)

        self.shotStrength_LineEdit = QLineEdit(self.support_GroupBox)
        self.shotStrength_LineEdit.setObjectName(u"shotStrength_LineEdit")
        self.shotStrength_LineEdit.setFont(font3)
        self.shotStrength_LineEdit.setReadOnly(True)

        self.shotcrete_GridLayout.addWidget(self.shotStrength_LineEdit, 1, 1, 1, 1)

        self.shotThickness_LineEdit = QLineEdit(self.support_GroupBox)
        self.shotThickness_LineEdit.setObjectName(u"shotThickness_LineEdit")
        self.shotThickness_LineEdit.setFont(font3)
        self.shotThickness_LineEdit.setReadOnly(True)

        self.shotcrete_GridLayout.addWidget(self.shotThickness_LineEdit, 1, 3, 1, 1)

        self.label_81 = QLabel(self.support_GroupBox)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font3)

        self.shotcrete_GridLayout.addWidget(self.label_81, 1, 2, 1, 1)

        self.shotcrete_GridLayout.setColumnStretch(0, 4)
        self.shotcrete_GridLayout.setColumnStretch(1, 5)
        self.shotcrete_GridLayout.setColumnStretch(2, 4)
        self.shotcrete_GridLayout.setColumnStretch(3, 5)

        self.verticalLayout_34.addLayout(self.shotcrete_GridLayout)

        self.line_3 = QFrame(self.support_GroupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.line_3)

        self.liner_GridLayout = QGridLayout()
        self.liner_GridLayout.setObjectName(u"liner_GridLayout")
        self.liner_GridLayout.setVerticalSpacing(0)
        self.liner_GridLayout.setContentsMargins(-1, -1, -1, 0)
        self.linerStrength_LineEdit = QLineEdit(self.support_GroupBox)
        self.linerStrength_LineEdit.setObjectName(u"linerStrength_LineEdit")
        self.linerStrength_LineEdit.setFont(font3)
        self.linerStrength_LineEdit.setReadOnly(True)

        self.liner_GridLayout.addWidget(self.linerStrength_LineEdit, 0, 1, 1, 1)

        self.label_84 = QLabel(self.support_GroupBox)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font3)

        self.liner_GridLayout.addWidget(self.label_84, 0, 2, 1, 1)

        self.label_83 = QLabel(self.support_GroupBox)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font3)

        self.liner_GridLayout.addWidget(self.label_83, 0, 0, 1, 1)

        self.linerThickness_LineEdit = QLineEdit(self.support_GroupBox)
        self.linerThickness_LineEdit.setObjectName(u"linerThickness_LineEdit")
        self.linerThickness_LineEdit.setFont(font3)
        self.linerThickness_LineEdit.setReadOnly(True)

        self.liner_GridLayout.addWidget(self.linerThickness_LineEdit, 0, 3, 1, 1)

        self.liner_GridLayout.setColumnStretch(0, 4)
        self.liner_GridLayout.setColumnStretch(1, 5)
        self.liner_GridLayout.setColumnStretch(2, 4)
        self.liner_GridLayout.setColumnStretch(3, 5)

        self.verticalLayout_34.addLayout(self.liner_GridLayout)

        self.line_4 = QFrame(self.support_GroupBox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.line_4)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, -1, -1, 0)
        self.label_71 = QLabel(self.support_GroupBox)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font3)

        self.horizontalLayout_21.addWidget(self.label_71)

        self.otherSupportRequest_LineEdit = QLineEdit(self.support_GroupBox)
        self.otherSupportRequest_LineEdit.setObjectName(u"otherSupportRequest_LineEdit")
        self.otherSupportRequest_LineEdit.setFont(font3)
        self.otherSupportRequest_LineEdit.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.otherSupportRequest_LineEdit)

        self.horizontalLayout_21.setStretch(0, 16)
        self.horizontalLayout_21.setStretch(1, 59)

        self.verticalLayout_34.addLayout(self.horizontalLayout_21)


        self.verticalLayout_6.addWidget(self.support_GroupBox)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.jammingCM_TextBrowser = QTextBrowser(Monitor_SubWidget)
        self.jammingCM_TextBrowser.setObjectName(u"jammingCM_TextBrowser")
        self.jammingCM_TextBrowser.setFont(font2)
        self.jammingCM_TextBrowser.setAutoFormatting(QTextEdit.AutoBulletList)

        self.gridLayout_3.addWidget(self.jammingCM_TextBrowser, 1, 1, 1, 1)

        self.label_9 = QLabel(Monitor_SubWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setTextFormat(Qt.AutoText)

        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_8 = QLabel(Monitor_SubWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.jammingRisk_LineEdit = QLineEdit(Monitor_SubWidget)
        self.jammingRisk_LineEdit.setObjectName(u"jammingRisk_LineEdit")
        self.jammingRisk_LineEdit.setFont(font2)
        self.jammingRisk_LineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.jammingRisk_LineEdit, 0, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 13)
        self.verticalLayout_2.setStretch(1, 7)

        self.retranslateUi(Monitor_SubWidget)

        QMetaObject.connectSlotsByName(Monitor_SubWidget)
    # setupUi

    def retranslateUi(self, Monitor_SubWidget):
        Monitor_SubWidget.setWindowTitle(QCoreApplication.translate("Monitor_SubWidget", u"\u6398\u8fdb\u72b6\u6001\u76d1\u63a7", None))
        self.muckImage_GroupBox.setTitle(QCoreApplication.translate("Monitor_SubWidget", u"\u5ca9\u6e23\u56fe\u50cf", None))
        self.muckImage_Label.setText("")
        self.label_33.setText("")
        self.label_12.setText(QCoreApplication.translate("Monitor_SubWidget", u"<html><head/><body><p align=\"center\">\u603b\u4f53\u79ef<br/>(m<span style=\" vertical-align:super;\">3</span>)</p></body></html>", None))
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("Monitor_SubWidget", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">d</span><span style=\" vertical-align:sub;\">50</span><br/>(mm)</p></body></html>", None))
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("Monitor_SubWidget", u"<html><head/><body><p><span style=\" font-style:italic;\">Cu</span></p></body></html>", None))
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("Monitor_SubWidget", u"<html><head/><body><p><span style=\" font-style:italic;\">Cc</span></p></body></html>", None))
        self.label_30.setText("")
        self.label_31.setText(QCoreApplication.translate("Monitor_SubWidget", u"<html><head/><body><p><span style=\" font-style:italic;\">CI</span></p></body></html>", None))
        self.label_34.setText("")
        self.label_7.setText("")
        self.label_11.setText(QCoreApplication.translate("Monitor_SubWidget", u"<html><head/><body><p align=\"center\">\u63a8\u8fdb\u901f\u5ea6<br>(mm/min)</p></body></html>", None))
        self.label_17.setText("")
        self.label_13.setText(QCoreApplication.translate("Monitor_SubWidget", u"<html><head/><body><p align=\"center\">\u603b\u63a8\u529b<br>(MN)</p></body></html>", None))
        self.label_18.setText("")
        self.label_14.setText(QCoreApplication.translate("Monitor_SubWidget", u"<html><head/><body><p align=\"center\">\u5200\u76d8\u8f6c\u901f<br>(r/min)</p></body></html>", None))
        self.label_19.setText("")
        self.label_15.setText(QCoreApplication.translate("Monitor_SubWidget", u"<html><head/><body><p align=\"center\">\u5200\u76d8\u626d\u77e9<br>(MN\u00b7m)</p></body></html>", None))
        self.label_20.setText("")
        self.label_16.setText(QCoreApplication.translate("Monitor_SubWidget", u"<html><head/><body><p align=\"center\">\u8d2f\u5165\u5ea6<br>(mm/r)</p></body></html>", None))
        self.label_10.setText("")
        self.rock_Curve_GroupBox.setTitle(QCoreApplication.translate("Monitor_SubWidget", u"\u56f4\u5ca9\u8d70\u52bf", None))
        self.basicInfo_GroupBox.setTitle(QCoreApplication.translate("Monitor_SubWidget", u"\u57fa\u672c\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u65f6\u95f4", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("Monitor_SubWidget", u"yyyy/M/d H:mm:ss", None))
        self.label_2.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u6869\u53f7", None))
        self.mileage_LineEdit.setText("")
        self.label_5.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u5f53\u524d\u72b6\u6001", None))
        self.status_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u505c\u673a", None))
        self.rockCondition_GroupBox.setTitle(QCoreApplication.translate("Monitor_SubWidget", u"\u56f4\u5ca9\u60c5\u51b5", None))
        self.rockGrade_LineEdit.setText("")
        self.ucs_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"MPa", None))
        self.label_6.setText(QCoreApplication.translate("Monitor_SubWidget", u"Kv", None))
        self.label_3.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u7ea7\u522b", None))
        self.kv_LineEdit.setText("")
        self.label_4.setText(QCoreApplication.translate("Monitor_SubWidget", u"UCS", None))
        self.suggestion_GroupBox.setTitle(QCoreApplication.translate("Monitor_SubWidget", u"\u6398\u8fdb\u5efa\u8bae", None))
        self.suggest_f_PerfMode_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"0", None))
        self.suggest_vr_PerfMode_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"0", None))
        self.label_22.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u5efa\u8bae\u63a8\u529b", None))
        self.suggest_f_EcoMode_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"0", None))
        self.label_92.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u7ecf\u6d4e\u6a21\u5f0f", None))
        self.label_93.setText(QCoreApplication.translate("Monitor_SubWidget", u"kN", None))
        self.label_23.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u5efa\u8bae\u8f6c\u901f", None))
        self.suggest_vr_EcoMode_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"0", None))
        self.label_90.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u6548\u7387\u6a21\u5f0f", None))
        self.label_94.setText(QCoreApplication.translate("Monitor_SubWidget", u"RPM", None))
        self.support_GroupBox.setTitle(QCoreApplication.translate("Monitor_SubWidget", u"\u652f\u62a4\u5efa\u8bae", None))
        self.label_77.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u73af\u5411\u95f4\u8ddd", None))
        self.boltLength_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"2.5~3.0  m", None))
        self.label_73.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u951a\u6746\u957f\u5ea6", None))
        self.boltModel_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u03c625", None))
        self.boltLongiSpacing_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"1.5~2.0  m", None))
        self.boltHoopSpacing_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"1.2~1.5  m", None))
        self.label_78.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u7eb5\u5411\u95f4\u8ddd", None))
        self.label_72.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u951a\u6746\u578b\u53f7", None))
        self.label_79.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u5e03\u8bbe\u8303\u56f4", None))
        self.boltRange_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"180\u00b0", None))
        self.label_75.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u62f1\u67b6\u578b\u53f7", None))
        self.archModel_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"HW100", None))
        self.label_74.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u62f1\u67b6\u95f4\u8ddd", None))
        self.archSpacing_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"1.5~2.0  m", None))
        self.label_85.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u94a2\u7b4b\u7f51\u578b\u53f7", None))
        self.shotInTime_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u5426", None))
        self.netRange_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"180\u00b0", None))
        self.label_82.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u662f\u5426\u5e94\u6025\u55b7", None))
        self.netModel_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u03c68\u00d7\u03c68@200", None))
        self.label_76.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u94a2\u7b4b\u7f51\u8303\u56f4", None))
        self.label_80.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u55b7\u783c\u5f3a\u5ea6", None))
        self.shotStrength_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"C30", None))
        self.shotThickness_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"15  cm", None))
        self.label_81.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u55b7\u783c\u539a\u5ea6", None))
        self.linerStrength_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"C35", None))
        self.label_84.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u886c\u780c\u539a\u5ea6", None))
        self.label_83.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u886c\u780c\u5f3a\u5ea6", None))
        self.linerThickness_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"30  cm", None))
        self.label_71.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u5176\u5b83\u8981\u6c42", None))
        self.jammingCM_TextBrowser.setHtml(QCoreApplication.translate("Monitor_SubWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:9px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7ef4\u6301\u6b63\u5e38\u63a8\u529b\u53ca\u8f6c\u901f\u3002</p>\n"
"<p style=\" margin-top:9px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5e73\u7a33\u8fde\u7eed\u6398\u8fdb\u3002</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u5361\u673a\u5bf9\u7b56", None))
        self.label_8.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u5361\u673a\u98ce\u9669", None))
        self.jammingRisk_LineEdit.setText(QCoreApplication.translate("Monitor_SubWidget", u"\u4f4e", None))
    # retranslateUi

