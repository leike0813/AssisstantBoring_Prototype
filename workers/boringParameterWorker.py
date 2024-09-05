import PySide2.QtCore as QtC
import numpy as np
import datetime
from .daemonWorker import DaemonWorker


class DummyBoringParameterWorker(DaemonWorker):
    sendBoringParameter = QtC.Signal(int, list)
    boringParameterSendingComplete = QtC.Signal(datetime.datetime, float)

    def __init__(self, daemonWidget=None, parent=None):
        super(DummyBoringParameterWorker, self).__init__(daemonWidget=daemonWidget, parent=parent)
        self.config = daemonWidget.mainWindow.config
        self.sample_pre = None
        self.sample_stable = None
        self.sample_end = None

        self.current_sample = None
        self.current_index = 0
        self.accumulate_index = 0
        self.mileage_increment = 0
        self.stop_signal_received = False

        self.timer = None

    @QtC.Slot(tuple, tuple, tuple)
    def onSampleReceived(self, sample_pre, sample_stable, sample_end):
        if not self._is_valid_sample(sample_pre) or not self._is_valid_sample(
                sample_stable) or not self._is_valid_sample(sample_end):
            raise ValueError('Invalid sample')
        self.sample_pre = sample_pre
        self.sample_stable = sample_stable
        self.sample_end = sample_end

        self.timer = QtC.QTimer()
        self.timer.timeout.connect(self._send_next)

    @QtC.Slot(datetime.datetime)
    def onStartSendBoringParameterSignalReceived(self, _time):
        self.current_sample = self.sample_pre
        self.current_index = 0
        self.accumulate_index = 0
        self.mileage_increment = 0
        self.stop_signal_received = False
        self._send_next()
        self.timer.start(1000)

    @QtC.Slot(datetime.datetime)
    def onStopSendBoringParameterSignalReceived(self, _time):
        if not self.stop_signal_received:
            self.stop_signal_received = True
            self.sample_end = (
                self.accumulate_index + np.arange(len(self.sample_end[0])),
                self.sample_end[1]
            )
            self.current_sample = self.sample_end
            self.current_index = 0
            self._send_next()

    def _send_next(self):
        if self.current_sample is not None and self.current_index < len(self.current_sample[0]):
            _timestamp = self.current_sample[0][self.current_index]
            _data = self.current_sample[1][self.current_index].tolist()
            self.mileage_increment += _data[0] / 60000
            self.sendBoringParameter.emit(_timestamp, _data)
            self.current_index += 1
            self.accumulate_index += 1
        elif self.current_sample is self.sample_pre:
            self.current_sample = self.sample_stable
            self.current_index = 0
        elif self.current_sample is self.sample_stable and self.current_index == len(self.current_sample[0]):
            self.sample_stable = (
                self.accumulate_index + np.arange(len(self.sample_stable[0])),
                self.sample_stable[1]
            )
            self.current_sample = self.sample_stable
            self.current_index = 0
        elif self.current_sample is self.sample_end and self.current_index == len(self.current_sample[0]):
            self.sample_pre = None
            self.sample_stable = None
            self.sample_end = None
            self.timer.stop()
            self.boringParameterSendingComplete.emit(datetime.datetime.now(), self.mileage_increment)

    def _is_valid_sample(self, sample):
        return isinstance(sample, tuple) and len(sample) == 2 and isinstance(sample[0], np.ndarray) and isinstance(
            sample[1], np.ndarray) and sample[0].ndim == 1 and sample[1].ndim == 2 and sample[0].shape[0] == \
            sample[1].shape[0] and sample[0].shape[0] > 0