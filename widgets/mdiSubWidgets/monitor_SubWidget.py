import PySide2.QtWidgets as QtW, PySide2.QtCore as QtC, PySide2.QtGui as QtG
import numpy as np
import datetime
from config import MPL_RC
from ui.mdiSubWidgets import Ui_Monitor_SubWidget


__all__ = ['Monitor_SubWidget']


class Monitor_SubWidget(QtW.QWidget, Ui_Monitor_SubWidget):
    def __init__(self, parent=None):
        super(Monitor_SubWidget, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
        # 初始化掘进参数绘图控件
        self.initializeBoringParameterPlotWidget()
        self.initializeMuckParameterPlotWidget()
        self.initializeRockInformationPlotWidget()
        self.clock_Timer = QtC.QTimer()
        self.clock_Timer.timeout.connect(self.updateClock)
        self.clock_Timer.start(1000)
        self.status_Timer = QtC.QTimer()
        self.status_Timer.setInterval(500)
        self.status_Timer.timeout.connect(self.changeStatusColor)

    def initUi(self):
        self.boringParameter_LCDList = [
            self.pr_LCD,
            self.f_LCD,
            self.vr_LCD,
            self.t_LCD,
            self.vp_LCD,
        ]
        self.muckParameter_LCDList = [
            self.vol_LCD,
            self.d50_LCD,
            self.cu_LCD,
            self.cc_LCD,
            self.ci_LCD,
        ]
        self.muckImage_Label.setSizePolicy(QtW.QSizePolicy.Ignored, QtW.QSizePolicy.Ignored)
        self.muckImage_Label.setScaledContents(True)

        self.boringColor1 = QtG.QColor("red")
        self.boringColor2 = QtG.QColor("orangered")
        self.idleColor = QtG.QColor("green")
        self.boringText = "掘进中..."
        self.idleText = "停机"

        self.status_LineEdit.setStyleSheet(f"color: {self.idleColor.name()}")


    @QtC.Slot()
    def updateClock(self):
        self.dateTimeEdit.setDateTime(QtC.QDateTime.currentDateTime())

    def initializeBoringParameterPlotWidget(self):
        data_schema = self.boringParameter_Curve_Widget.get_default_data_schema(5)
        data_schema.set_subplot_params(0, ylabel='$PR$(mm/min)', color='#0C5DA5', ylim=(0, 80))
        data_schema.set_subplot_params(1, ylabel='$F$(MN)', color='#00B945', ylim=(0, 20))
        data_schema.set_subplot_params(2, ylabel='$V_{R}$(r/min)', color='#FF9500', ylim=(0, 10))
        data_schema.set_subplot_params(3, ylabel='$T$(MN·m)', color='#FF2C00', ylim=(0, 2))
        data_schema.set_subplot_params(4, ylabel='$V_{P}$(mm/r)', color='#845B97', ylim=(0, 20))

        self.boringParameter_Curve_Widget.initPlot(
            data_schema=data_schema,
            xlabel='Time(s)',
            truncate=False,
            max_xrange=1000,
            xtick_interval=100,
        )

    def initializeMuckParameterPlotWidget(self):
        data_schema = self.muckParameter_Curve_Widget.get_default_data_schema(5)
        data_schema.set_subplot_params(0, ylabel='$V_{\mathrm{Total}}$(m$^{3}$)', color='#0C5DA5', plot_type='scatter', ylim=(0, 10))
        data_schema.set_subplot_params(1, ylabel='$d_{50}$(mm)', color='#00B945', plot_type='scatter', ylim=(0, 200))
        data_schema.set_subplot_params(2, ylabel='$Cu$', color='#FF9500', plot_type='scatter', ylim=(0, 30))
        data_schema.set_subplot_params(3, ylabel='$Cc$', color='#FF2C00', plot_type='scatter', ylim=(0.0, 1.0))
        data_schema.set_subplot_params(4, ylabel='$CI$', color='#845B97', plot_type='scatter', ylim=(100, 500))

        self.muckParameter_Curve_Widget.initPlot(
            data_schema=data_schema,
            xlabel='Time(s)',
            truncate=False,
            max_xrange=1000,
            xtick_interval=100,
        )

    def initializeRockInformationPlotWidget(self):
        data_schema = self.rockInformation_Curve_Widget.get_default_data_schema(3)
        data_schema.set_subplot_params(0, ylabel='Grade', color='#004488', marker_size=3, ylim=(-0.2, 4.2), yticks={0: 'II', 1: 'IIIa', 2: 'IIIb', 3: 'IV', 4: 'V'})
        data_schema.set_subplot_params(1, ylabel='$UCS$(MPa)', color='#DDAA33', marker_size=3, ylim=(0, 200))
        data_schema.set_subplot_params(2, ylabel='$K_{\mathrm{V}}$', color='#BB5566', marker_size=3, ylim=(0, 1))

        self.rockInformation_Curve_Widget.initPlot(
            data_schema=data_schema,
            xlabel='Mileage',
            truncate=True,
            max_xrange=200,
            xtick_interval=20,
        )

    def plot(self, widget_no, x, params):
        if widget_no == 0:
            LCDList = self.boringParameter_LCDList
        elif widget_no == 1:
            LCDList = self.muckParameter_LCDList
        elif widget_no == 2:
            LCDList = None
        else:
            raise NotImplementedError('widget_no must be 0, 1 or 2')

        widget = [
            self.boringParameter_Curve_Widget,
            self.muckParameter_Curve_Widget,
            self.rockInformation_Curve_Widget,
        ][widget_no]

        assert len(params) == {0: 5, 1: 5, 2: 3}[widget_no], 'Invalid number of params'

        widget.plot(x, [[param] for param in params])
        if LCDList is not None:
            for i, lcd in enumerate(LCDList):
                lcd.display(np.format_float_positional(
                    params[i],
                    precision=4,
                    unique=False,
                    fractional=False,
                    trim='k'
                ))

    @QtC.Slot(int, list)
    @QtC.Slot(float, list)
    def plotBoringParameter(self, time, params):
        self.plot(0, time, params)

    @QtC.Slot(int, list)
    @QtC.Slot(float, list)
    def plotMuckParameter(self, time, params):
        self.plot(1, time, params)

    @QtC.Slot(int, list)
    @QtC.Slot(float, list)
    def plotRockInformation(self, mileage, params):
        self.plot(2, mileage, params)

    @QtC.Slot(np.ndarray)
    def plotMuckImage(self, image_array):
        self.muckImage_Label.setPixmap(
            QtG.QPixmap.fromImage(
                QtG.QImage(
                    image_array.data,
                    image_array.shape[1],
                    image_array.shape[0],
                    QtG.QImage.Format_BGR888
                )
            )
        )

    @QtC.Slot(str, str, float, float, int, int, float, float, dict)
    def showMileageInformation(self, mileage_text, grade_text, ucs, kv, suggest_f_eco, suggest_f_perf,
                               suggest_vr_eco, suggest_vr_perf, other_dict):
        self.mileage_LineEdit.setText(mileage_text)
        self.rockGrade_LineEdit.setText(grade_text)
        self.ucs_LineEdit.setText("{ucs:.2f} MPa".format(ucs=ucs))
        self.kv_LineEdit.setText("{kv:.1f}".format(kv=kv))
        self.suggest_f_EcoMode_LineEdit.setText(str(suggest_f_eco))
        self.suggest_f_PerfMode_LineEdit.setText(str(suggest_f_perf))
        self.suggest_vr_EcoMode_LineEdit.setText("{vr:.1f}".format(vr=suggest_vr_eco))
        self.suggest_vr_PerfMode_LineEdit.setText("{vr:.1f}".format(vr=suggest_vr_perf))

        self.boltModel_LineEdit.setText(other_dict['bolt_spec'])
        self.boltLength_LineEdit.setText(other_dict['bolt_length'])
        self.boltHoopSpacing_LineEdit.setText(other_dict['bolt_cir_spacing'])
        self.boltLongiSpacing_LineEdit.setText(other_dict['bolt_longi_spacing'])
        self.boltRange_LineEdit.setText(other_dict['bolt_angle'])
        self.archModel_LineEdit.setText(other_dict['arch_spec'])
        self.archSpacing_LineEdit.setText(other_dict['arch_spacing'])
        self.netModel_LineEdit.setText(other_dict['net_spec'])
        self.netRange_LineEdit.setText(other_dict['net_angle'])
        self.shotStrength_LineEdit.setText(other_dict['shotcrete_strength'])
        self.shotThickness_LineEdit.setText(other_dict['shotcrete_thickness'])
        self.shotInTime_LineEdit.setText(other_dict['shotcrete_in_time'])
        self.linerStrength_LineEdit.setText(other_dict['liner_strength'])
        self.linerThickness_LineEdit.setText(other_dict['liner_thickness'])
        self.otherSupportRequest_LineEdit.setText(other_dict['others'])
        self.jammingRisk_LineEdit.setText(other_dict['jamming_risk'])
        self.jammingCM_TextBrowser.setText(other_dict['jamming_measure'])


    @QtC.Slot(datetime.datetime, float)
    def onStartBoringCycleSignalReceived(self, beginTime, beginMileage):
        self.boringParameter_Curve_Widget.reset()
        self.muckParameter_Curve_Widget.reset()
        self.status_LineEdit.setText(self.boringText)
        self.status_Timer.start()

    @QtC.Slot(datetime.datetime, float)
    def onStopBoringCycleSignalReceived(self, endTime, endMileage):
        self.status_Timer.stop()
        self.status_LineEdit.setText(self.idleText)
        self.status_LineEdit.setStyleSheet(f"color: {self.idleColor.name()}")

    @QtC.Slot()
    def changeStatusColor(self):
        currentColor = QtG.QColor(self.status_LineEdit.palette().text().color())
        newColor = self.boringColor1 if currentColor == self.boringColor2 else self.boringColor2
        self.status_LineEdit.setStyleSheet(f"color: {newColor.name()}")