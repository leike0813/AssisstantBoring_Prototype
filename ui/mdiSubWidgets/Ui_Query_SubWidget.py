# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Query_SubWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Query_SubWidget(object):
    def setupUi(self, Query_SubWidget):
        if not Query_SubWidget.objectName():
            Query_SubWidget.setObjectName(u"Query_SubWidget")
        Query_SubWidget.resize(680, 650)
        self.verticalLayout = QVBoxLayout(Query_SubWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget_2 = QTabWidget(Query_SubWidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_2.setFont(font)
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_26 = QVBoxLayout(self.tab_6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_105 = QLabel(self.tab_6)
        self.label_105.setObjectName(u"label_105")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_105.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_105)

        self.boringRecord_TBMID_ComboBox = QComboBox(self.tab_6)
        self.boringRecord_TBMID_ComboBox.addItem("")
        self.boringRecord_TBMID_ComboBox.setObjectName(u"boringRecord_TBMID_ComboBox")
        self.boringRecord_TBMID_ComboBox.setMaximumSize(QSize(40, 16777215))
        self.boringRecord_TBMID_ComboBox.setFont(font1)

        self.horizontalLayout_15.addWidget(self.boringRecord_TBMID_ComboBox)

        self.label_59 = QLabel(self.tab_6)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_59)

        self.boringRecord_DateEdit = QDateEdit(self.tab_6)
        self.boringRecord_DateEdit.setObjectName(u"boringRecord_DateEdit")
        self.boringRecord_DateEdit.setFont(font1)
        self.boringRecord_DateEdit.setDateTime(QDateTime(QDate(2018, 6, 25), QTime(0, 0, 0)))

        self.horizontalLayout_15.addWidget(self.boringRecord_DateEdit)

        self.label_60 = QLabel(self.tab_6)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_60)

        self.boringRecord_StartTime_DateTimeEdit = QDateTimeEdit(self.tab_6)
        self.boringRecord_StartTime_DateTimeEdit.setObjectName(u"boringRecord_StartTime_DateTimeEdit")
        self.boringRecord_StartTime_DateTimeEdit.setFont(font1)

        self.horizontalLayout_15.addWidget(self.boringRecord_StartTime_DateTimeEdit)

        self.label_61 = QLabel(self.tab_6)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_61)

        self.boringRecord_EndTime_DateTimeEdit = QDateTimeEdit(self.tab_6)
        self.boringRecord_EndTime_DateTimeEdit.setObjectName(u"boringRecord_EndTime_DateTimeEdit")
        self.boringRecord_EndTime_DateTimeEdit.setFont(font1)
        self.boringRecord_EndTime_DateTimeEdit.setTime(QTime(23, 59, 0))

        self.horizontalLayout_15.addWidget(self.boringRecord_EndTime_DateTimeEdit)

        self.boringRecord_Query_PushButton = QPushButton(self.tab_6)
        self.boringRecord_Query_PushButton.setObjectName(u"boringRecord_Query_PushButton")
        self.boringRecord_Query_PushButton.setFont(font1)

        self.horizontalLayout_15.addWidget(self.boringRecord_Query_PushButton)

        self.boringRecord_Export_PushButton = QPushButton(self.tab_6)
        self.boringRecord_Export_PushButton.setObjectName(u"boringRecord_Export_PushButton")
        self.boringRecord_Export_PushButton.setFont(font1)

        self.horizontalLayout_15.addWidget(self.boringRecord_Export_PushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)


        self.verticalLayout_26.addLayout(self.horizontalLayout_15)

        self.boringRecord_TableView = QTableView(self.tab_6)
        self.boringRecord_TableView.setObjectName(u"boringRecord_TableView")

        self.verticalLayout_26.addWidget(self.boringRecord_TableView)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_27 = QVBoxLayout(self.tab_7)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_106 = QLabel(self.tab_7)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_106)

        self.dailyReport_TBMID_ComboBox = QComboBox(self.tab_7)
        self.dailyReport_TBMID_ComboBox.addItem("")
        self.dailyReport_TBMID_ComboBox.setObjectName(u"dailyReport_TBMID_ComboBox")
        self.dailyReport_TBMID_ComboBox.setMaximumSize(QSize(40, 16777215))
        self.dailyReport_TBMID_ComboBox.setFont(font1)

        self.horizontalLayout_16.addWidget(self.dailyReport_TBMID_ComboBox)

        self.label_62 = QLabel(self.tab_7)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_62)

        self.dailyReport_DateEdit = QDateEdit(self.tab_7)
        self.dailyReport_DateEdit.setObjectName(u"dailyReport_DateEdit")
        self.dailyReport_DateEdit.setFont(font1)
        self.dailyReport_DateEdit.setDateTime(QDateTime(QDate(2018, 6, 25), QTime(0, 0, 0)))

        self.horizontalLayout_16.addWidget(self.dailyReport_DateEdit)

        self.dailyReport_Query_PushButton = QPushButton(self.tab_7)
        self.dailyReport_Query_PushButton.setObjectName(u"dailyReport_Query_PushButton")
        self.dailyReport_Query_PushButton.setFont(font1)

        self.horizontalLayout_16.addWidget(self.dailyReport_Query_PushButton)

        self.dailyReport_Export_PushButton = QPushButton(self.tab_7)
        self.dailyReport_Export_PushButton.setObjectName(u"dailyReport_Export_PushButton")
        self.dailyReport_Export_PushButton.setFont(font1)

        self.horizontalLayout_16.addWidget(self.dailyReport_Export_PushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)


        self.verticalLayout_27.addLayout(self.horizontalLayout_16)

        self.tableView_2 = QTableView(self.tab_7)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_27.addWidget(self.tableView_2)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_28 = QVBoxLayout(self.tab_8)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_63 = QLabel(self.tab_8)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_63)

        self.geology_StartMileage_SpinBox = QSpinBox(self.tab_8)
        self.geology_StartMileage_SpinBox.setObjectName(u"geology_StartMileage_SpinBox")
        self.geology_StartMileage_SpinBox.setMinimumSize(QSize(80, 0))
        self.geology_StartMileage_SpinBox.setFont(font1)

        self.horizontalLayout_17.addWidget(self.geology_StartMileage_SpinBox)

        self.label_64 = QLabel(self.tab_8)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_64)

        self.geology_EndMileage_SpinBox = QSpinBox(self.tab_8)
        self.geology_EndMileage_SpinBox.setObjectName(u"geology_EndMileage_SpinBox")
        self.geology_EndMileage_SpinBox.setMinimumSize(QSize(80, 0))
        self.geology_EndMileage_SpinBox.setFont(font1)

        self.horizontalLayout_17.addWidget(self.geology_EndMileage_SpinBox)

        self.geology_Query_PushButton = QPushButton(self.tab_8)
        self.geology_Query_PushButton.setObjectName(u"geology_Query_PushButton")
        self.geology_Query_PushButton.setFont(font1)

        self.horizontalLayout_17.addWidget(self.geology_Query_PushButton)

        self.geology_Export_PushButton = QPushButton(self.tab_8)
        self.geology_Export_PushButton.setObjectName(u"geology_Export_PushButton")
        self.geology_Export_PushButton.setFont(font1)

        self.horizontalLayout_17.addWidget(self.geology_Export_PushButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_5)


        self.verticalLayout_28.addLayout(self.horizontalLayout_17)

        self.tableView_3 = QTableView(self.tab_8)
        self.tableView_3.setObjectName(u"tableView_3")

        self.verticalLayout_28.addWidget(self.tableView_3)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.horizontalLayout_18 = QHBoxLayout(self.tab_9)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_65 = QLabel(self.tab_9)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font1)

        self.horizontalLayout_19.addWidget(self.label_65)

        self.support_Type_ComboBox = QComboBox(self.tab_9)
        self.support_Type_ComboBox.addItem("")
        self.support_Type_ComboBox.setObjectName(u"support_Type_ComboBox")
        self.support_Type_ComboBox.setFont(font1)

        self.horizontalLayout_19.addWidget(self.support_Type_ComboBox)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_6)


        self.verticalLayout_33.addLayout(self.horizontalLayout_19)

        self.groupBox_6 = QGroupBox(self.tab_9)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font1)
        self.gridLayout_13 = QGridLayout(self.groupBox_6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_66 = QLabel(self.groupBox_6)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_13.addWidget(self.label_66, 0, 0, 1, 1)

        self.label_67 = QLabel(self.groupBox_6)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_13.addWidget(self.label_67, 0, 2, 1, 1)

        self.support_BoltLength_LineEdit = QLineEdit(self.groupBox_6)
        self.support_BoltLength_LineEdit.setObjectName(u"support_BoltLength_LineEdit")
        self.support_BoltLength_LineEdit.setReadOnly(True)

        self.gridLayout_13.addWidget(self.support_BoltLength_LineEdit, 0, 3, 1, 1)

        self.label_68 = QLabel(self.groupBox_6)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_13.addWidget(self.label_68, 1, 0, 1, 1)

        self.support_BoltHoopSpacing_LineEdit = QLineEdit(self.groupBox_6)
        self.support_BoltHoopSpacing_LineEdit.setObjectName(u"support_BoltHoopSpacing_LineEdit")
        self.support_BoltHoopSpacing_LineEdit.setReadOnly(True)

        self.gridLayout_13.addWidget(self.support_BoltHoopSpacing_LineEdit, 1, 1, 1, 1)

        self.label_69 = QLabel(self.groupBox_6)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_13.addWidget(self.label_69, 1, 2, 1, 1)

        self.support_BoltLongiSpacing_LineEdit = QLineEdit(self.groupBox_6)
        self.support_BoltLongiSpacing_LineEdit.setObjectName(u"support_BoltLongiSpacing_LineEdit")
        self.support_BoltLongiSpacing_LineEdit.setReadOnly(True)

        self.gridLayout_13.addWidget(self.support_BoltLongiSpacing_LineEdit, 1, 3, 1, 1)

        self.support_BoltType_LineEdit = QLineEdit(self.groupBox_6)
        self.support_BoltType_LineEdit.setObjectName(u"support_BoltType_LineEdit")
        self.support_BoltType_LineEdit.setReadOnly(True)

        self.gridLayout_13.addWidget(self.support_BoltType_LineEdit, 0, 1, 1, 1)

        self.label_70 = QLabel(self.groupBox_6)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_13.addWidget(self.label_70, 2, 0, 1, 1)

        self.support_BoltRange_LineEdit = QLineEdit(self.groupBox_6)
        self.support_BoltRange_LineEdit.setObjectName(u"support_BoltRange_LineEdit")
        self.support_BoltRange_LineEdit.setReadOnly(True)

        self.gridLayout_13.addWidget(self.support_BoltRange_LineEdit, 2, 1, 1, 1)

        self.gridLayout_13.setColumnStretch(0, 2)
        self.gridLayout_13.setColumnStretch(1, 4)
        self.gridLayout_13.setColumnStretch(2, 2)
        self.gridLayout_13.setColumnStretch(3, 4)

        self.verticalLayout_33.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.tab_9)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font1)
        self.gridLayout_14 = QGridLayout(self.groupBox_7)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_107 = QLabel(self.groupBox_7)
        self.label_107.setObjectName(u"label_107")

        self.gridLayout_14.addWidget(self.label_107, 0, 0, 1, 1)

        self.support_ArchModel_LineEdit = QLineEdit(self.groupBox_7)
        self.support_ArchModel_LineEdit.setObjectName(u"support_ArchModel_LineEdit")
        self.support_ArchModel_LineEdit.setReadOnly(True)

        self.gridLayout_14.addWidget(self.support_ArchModel_LineEdit, 0, 1, 1, 1)

        self.label_108 = QLabel(self.groupBox_7)
        self.label_108.setObjectName(u"label_108")

        self.gridLayout_14.addWidget(self.label_108, 0, 2, 1, 1)

        self.support_ArchSpacing_LineEdit = QLineEdit(self.groupBox_7)
        self.support_ArchSpacing_LineEdit.setObjectName(u"support_ArchSpacing_LineEdit")
        self.support_ArchSpacing_LineEdit.setReadOnly(True)

        self.gridLayout_14.addWidget(self.support_ArchSpacing_LineEdit, 0, 3, 1, 1)

        self.gridLayout_14.setColumnStretch(0, 2)
        self.gridLayout_14.setColumnStretch(1, 4)
        self.gridLayout_14.setColumnStretch(2, 2)
        self.gridLayout_14.setColumnStretch(3, 4)

        self.verticalLayout_33.addWidget(self.groupBox_7)

        self.groupBox_18 = QGroupBox(self.tab_9)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setFont(font1)
        self.gridLayout_15 = QGridLayout(self.groupBox_18)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_109 = QLabel(self.groupBox_18)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout_15.addWidget(self.label_109, 0, 0, 1, 1)

        self.support_NetModel_LineEdit = QLineEdit(self.groupBox_18)
        self.support_NetModel_LineEdit.setObjectName(u"support_NetModel_LineEdit")
        self.support_NetModel_LineEdit.setReadOnly(True)

        self.gridLayout_15.addWidget(self.support_NetModel_LineEdit, 0, 1, 1, 1)

        self.label_110 = QLabel(self.groupBox_18)
        self.label_110.setObjectName(u"label_110")

        self.gridLayout_15.addWidget(self.label_110, 0, 2, 1, 1)

        self.support_NetRange_LineEdit = QLineEdit(self.groupBox_18)
        self.support_NetRange_LineEdit.setObjectName(u"support_NetRange_LineEdit")
        self.support_NetRange_LineEdit.setReadOnly(True)

        self.gridLayout_15.addWidget(self.support_NetRange_LineEdit, 0, 3, 1, 1)

        self.label_111 = QLabel(self.groupBox_18)
        self.label_111.setObjectName(u"label_111")

        self.gridLayout_15.addWidget(self.label_111, 1, 0, 1, 1)

        self.support_ShotStrength_LineEdit = QLineEdit(self.groupBox_18)
        self.support_ShotStrength_LineEdit.setObjectName(u"support_ShotStrength_LineEdit")
        self.support_ShotStrength_LineEdit.setReadOnly(True)

        self.gridLayout_15.addWidget(self.support_ShotStrength_LineEdit, 1, 1, 1, 1)

        self.label_112 = QLabel(self.groupBox_18)
        self.label_112.setObjectName(u"label_112")

        self.gridLayout_15.addWidget(self.label_112, 1, 2, 1, 1)

        self.support_ShotThickness_LineEdit = QLineEdit(self.groupBox_18)
        self.support_ShotThickness_LineEdit.setObjectName(u"support_ShotThickness_LineEdit")
        self.support_ShotThickness_LineEdit.setReadOnly(True)

        self.gridLayout_15.addWidget(self.support_ShotThickness_LineEdit, 1, 3, 1, 1)

        self.label_113 = QLabel(self.groupBox_18)
        self.label_113.setObjectName(u"label_113")

        self.gridLayout_15.addWidget(self.label_113, 2, 0, 1, 1)

        self.support_ShotInTime_LineEdit = QLineEdit(self.groupBox_18)
        self.support_ShotInTime_LineEdit.setObjectName(u"support_ShotInTime_LineEdit")
        self.support_ShotInTime_LineEdit.setReadOnly(True)

        self.gridLayout_15.addWidget(self.support_ShotInTime_LineEdit, 2, 1, 1, 1)

        self.gridLayout_15.setColumnStretch(0, 2)
        self.gridLayout_15.setColumnStretch(1, 4)
        self.gridLayout_15.setColumnStretch(2, 2)
        self.gridLayout_15.setColumnStretch(3, 4)

        self.verticalLayout_33.addWidget(self.groupBox_18)

        self.groupBox_19 = QGroupBox(self.tab_9)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setFont(font1)
        self.gridLayout_16 = QGridLayout(self.groupBox_19)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.support_LinerStrength_LineEdit = QLineEdit(self.groupBox_19)
        self.support_LinerStrength_LineEdit.setObjectName(u"support_LinerStrength_LineEdit")
        self.support_LinerStrength_LineEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.support_LinerStrength_LineEdit, 0, 1, 1, 1)

        self.label_114 = QLabel(self.groupBox_19)
        self.label_114.setObjectName(u"label_114")

        self.gridLayout_16.addWidget(self.label_114, 0, 0, 1, 1)

        self.label_115 = QLabel(self.groupBox_19)
        self.label_115.setObjectName(u"label_115")

        self.gridLayout_16.addWidget(self.label_115, 0, 2, 1, 1)

        self.support_LinerThickness_LineEdit = QLineEdit(self.groupBox_19)
        self.support_LinerThickness_LineEdit.setObjectName(u"support_LinerThickness_LineEdit")
        self.support_LinerThickness_LineEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.support_LinerThickness_LineEdit, 0, 3, 1, 1)

        self.gridLayout_16.setColumnStretch(0, 2)
        self.gridLayout_16.setColumnStretch(1, 4)
        self.gridLayout_16.setColumnStretch(2, 2)
        self.gridLayout_16.setColumnStretch(3, 4)

        self.verticalLayout_33.addWidget(self.groupBox_19)

        self.groupBox_20 = QGroupBox(self.tab_9)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setFont(font1)
        self.verticalLayout_36 = QVBoxLayout(self.groupBox_20)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.support_OtherSupportRequest_TextBrowser = QTextBrowser(self.groupBox_20)
        self.support_OtherSupportRequest_TextBrowser.setObjectName(u"support_OtherSupportRequest_TextBrowser")

        self.verticalLayout_36.addWidget(self.support_OtherSupportRequest_TextBrowser)


        self.verticalLayout_33.addWidget(self.groupBox_20)

        self.verticalLayout_33.setStretch(0, 1)
        self.verticalLayout_33.setStretch(1, 2)
        self.verticalLayout_33.setStretch(2, 1)
        self.verticalLayout_33.setStretch(3, 2)
        self.verticalLayout_33.setStretch(4, 1)
        self.verticalLayout_33.setStretch(5, 4)

        self.horizontalLayout_18.addLayout(self.verticalLayout_33)

        self.groupBox_21 = QGroupBox(self.tab_9)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setFont(font1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_21)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.supportLongitudinal_Label = QLabel(self.groupBox_21)
        self.supportLongitudinal_Label.setObjectName(u"supportLongitudinal_Label")

        self.verticalLayout_2.addWidget(self.supportLongitudinal_Label)

        self.supportCrossSectional_Label = QLabel(self.groupBox_21)
        self.supportCrossSectional_Label.setObjectName(u"supportCrossSectional_Label")

        self.verticalLayout_2.addWidget(self.supportCrossSectional_Label)


        self.horizontalLayout_18.addWidget(self.groupBox_21)

        self.horizontalLayout_18.setStretch(0, 4)
        self.horizontalLayout_18.setStretch(1, 6)
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.verticalLayout_35 = QVBoxLayout(self.tab_10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_116 = QLabel(self.tab_10)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setFont(font1)

        self.horizontalLayout_20.addWidget(self.label_116)

        self.customQuery_SQL_LineEdit = QLineEdit(self.tab_10)
        self.customQuery_SQL_LineEdit.setObjectName(u"customQuery_SQL_LineEdit")
        self.customQuery_SQL_LineEdit.setFont(font1)

        self.horizontalLayout_20.addWidget(self.customQuery_SQL_LineEdit)

        self.customQuery_Query_PushButton = QPushButton(self.tab_10)
        self.customQuery_Query_PushButton.setObjectName(u"customQuery_Query_PushButton")
        self.customQuery_Query_PushButton.setFont(font1)

        self.horizontalLayout_20.addWidget(self.customQuery_Query_PushButton)

        self.customQuery_Export_PushButton = QPushButton(self.tab_10)
        self.customQuery_Export_PushButton.setObjectName(u"customQuery_Export_PushButton")
        self.customQuery_Export_PushButton.setFont(font1)

        self.horizontalLayout_20.addWidget(self.customQuery_Export_PushButton)


        self.verticalLayout_35.addLayout(self.horizontalLayout_20)

        self.customQuery_TableView = QTableView(self.tab_10)
        self.customQuery_TableView.setObjectName(u"customQuery_TableView")

        self.verticalLayout_35.addWidget(self.customQuery_TableView)

        self.tabWidget_2.addTab(self.tab_10, "")

        self.verticalLayout.addWidget(self.tabWidget_2)


        self.retranslateUi(Query_SubWidget)

        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Query_SubWidget)
    # setupUi

    def retranslateUi(self, Query_SubWidget):
        Query_SubWidget.setWindowTitle(QCoreApplication.translate("Query_SubWidget", u"\u6570\u636e\u67e5\u8be2", None))
        self.label_105.setText(QCoreApplication.translate("Query_SubWidget", u"TBM\u7f16\u53f7", None))
        self.boringRecord_TBMID_ComboBox.setItemText(0, QCoreApplication.translate("Query_SubWidget", u"1", None))

        self.label_59.setText(QCoreApplication.translate("Query_SubWidget", u"\u65e5\u671f", None))
        self.label_60.setText(QCoreApplication.translate("Query_SubWidget", u"\u8d77\u59cb\u65f6\u95f4", None))
        self.boringRecord_StartTime_DateTimeEdit.setDisplayFormat(QCoreApplication.translate("Query_SubWidget", u"H:mm", None))
        self.label_61.setText(QCoreApplication.translate("Query_SubWidget", u"\u7ed3\u675f\u65f6\u95f4", None))
        self.boringRecord_EndTime_DateTimeEdit.setDisplayFormat(QCoreApplication.translate("Query_SubWidget", u"H:mm", None))
        self.boringRecord_Query_PushButton.setText(QCoreApplication.translate("Query_SubWidget", u"\u8bfb\u53d6", None))
        self.boringRecord_Export_PushButton.setText(QCoreApplication.translate("Query_SubWidget", u"\u5bfc\u51fa", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("Query_SubWidget", u"TBM\u8fd0\u884c\u72b6\u6001\u8bb0\u5f55", None))
        self.label_106.setText(QCoreApplication.translate("Query_SubWidget", u"TBM\u7f16\u53f7", None))
        self.dailyReport_TBMID_ComboBox.setItemText(0, QCoreApplication.translate("Query_SubWidget", u"1", None))

        self.label_62.setText(QCoreApplication.translate("Query_SubWidget", u"\u65e5\u671f", None))
        self.dailyReport_Query_PushButton.setText(QCoreApplication.translate("Query_SubWidget", u"\u8bfb\u53d6", None))
        self.dailyReport_Export_PushButton.setText(QCoreApplication.translate("Query_SubWidget", u"\u5bfc\u51fa", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("Query_SubWidget", u"\u6398\u8fdb\u62a5\u8868", None))
        self.label_63.setText(QCoreApplication.translate("Query_SubWidget", u"\u8d77\u59cb\u6869\u53f7", None))
        self.label_64.setText(QCoreApplication.translate("Query_SubWidget", u"\u7ed3\u675f\u6869\u53f7", None))
        self.geology_Query_PushButton.setText(QCoreApplication.translate("Query_SubWidget", u"\u8bfb\u53d6", None))
        self.geology_Export_PushButton.setText(QCoreApplication.translate("Query_SubWidget", u"\u5bfc\u51fa", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("Query_SubWidget", u"\u5730\u8d28\u60c5\u51b5", None))
        self.label_65.setText(QCoreApplication.translate("Query_SubWidget", u"\u652f\u62a4\u7c7b\u578b", None))
        self.support_Type_ComboBox.setItemText(0, QCoreApplication.translate("Query_SubWidget", u"IVa\u578b", None))

        self.groupBox_6.setTitle(QCoreApplication.translate("Query_SubWidget", u"\u951a\u6746", None))
        self.label_66.setText(QCoreApplication.translate("Query_SubWidget", u"\u578b\u53f7", None))
        self.label_67.setText(QCoreApplication.translate("Query_SubWidget", u"\u957f\u5ea6", None))
        self.support_BoltLength_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"2.5~3.0  m", None))
        self.label_68.setText(QCoreApplication.translate("Query_SubWidget", u"\u73af\u5411\u95f4\u8ddd", None))
        self.support_BoltHoopSpacing_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"1.2~1.5  m", None))
        self.label_69.setText(QCoreApplication.translate("Query_SubWidget", u"\u7eb5\u5411\u95f4\u8ddd", None))
        self.support_BoltLongiSpacing_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"1.2~1.5  m", None))
        self.support_BoltType_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"\u03c625", None))
        self.label_70.setText(QCoreApplication.translate("Query_SubWidget", u"\u5e03\u8bbe\u8303\u56f4", None))
        self.support_BoltRange_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"180\u00b0", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Query_SubWidget", u"\u62f1\u67b6", None))
        self.label_107.setText(QCoreApplication.translate("Query_SubWidget", u"\u578b\u53f7", None))
        self.support_ArchModel_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"HW125", None))
        self.label_108.setText(QCoreApplication.translate("Query_SubWidget", u"\u95f4\u8ddd", None))
        self.support_ArchSpacing_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"1.2~1.5  m", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("Query_SubWidget", u"\u55b7\u5c04\u6df7\u51dd\u571f", None))
        self.label_109.setText(QCoreApplication.translate("Query_SubWidget", u"\u94a2\u7b4b\u7f51\u578b\u53f7", None))
        self.support_NetModel_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"\u03c68\u00d7\u03c68@200", None))
        self.label_110.setText(QCoreApplication.translate("Query_SubWidget", u"\u94a2\u7b4b\u7f51\u8303\u56f4", None))
        self.support_NetRange_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"180\u00b0", None))
        self.label_111.setText(QCoreApplication.translate("Query_SubWidget", u"\u55b7\u783c\u5f3a\u5ea6", None))
        self.support_ShotStrength_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"C30", None))
        self.label_112.setText(QCoreApplication.translate("Query_SubWidget", u"\u55b7\u783c\u539a\u5ea6", None))
        self.support_ShotThickness_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"15  cm", None))
        self.label_113.setText(QCoreApplication.translate("Query_SubWidget", u"\u662f\u5426\u5e94\u6025\u55b7", None))
        self.support_ShotInTime_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"\u5426", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("Query_SubWidget", u"\u886c\u780c", None))
        self.support_LinerStrength_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"C35", None))
        self.label_114.setText(QCoreApplication.translate("Query_SubWidget", u"\u5f3a\u5ea6", None))
        self.label_115.setText(QCoreApplication.translate("Query_SubWidget", u"\u539a\u5ea6", None))
        self.support_LinerThickness_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"30  cm", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("Query_SubWidget", u"\u5176\u4ed6\u8981\u6c42", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("Query_SubWidget", u"\u652f\u62a4\u793a\u610f\u56fe", None))
        self.supportLongitudinal_Label.setText("")
        self.supportCrossSectional_Label.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("Query_SubWidget", u"\u652f\u62a4\u53c2\u6570", None))
        self.label_116.setText(QCoreApplication.translate("Query_SubWidget", u"\u81ea\u5b9a\u4e49\u67e5\u8be2\u8bed\u53e5(SQL)", None))
        self.customQuery_SQL_LineEdit.setText(QCoreApplication.translate("Query_SubWidget", u"select * from daily_report", None))
        self.customQuery_Query_PushButton.setText(QCoreApplication.translate("Query_SubWidget", u"\u8bfb\u53d6", None))
        self.customQuery_Export_PushButton.setText(QCoreApplication.translate("Query_SubWidget", u"\u5bfc\u51fa", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), QCoreApplication.translate("Query_SubWidget", u"\u81ea\u5b9a\u4e49\u67e5\u8be2", None))
    # retranslateUi

