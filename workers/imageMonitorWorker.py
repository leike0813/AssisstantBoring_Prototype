import os
import datetime
from pathlib import Path
import PySide2.QtWidgets as QtW, PySide2.QtCore as QtC
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .daemonWorker import DaemonWorker


class ImageMonitorWorker(DaemonWorker):
    findNewImage = QtC.Signal(datetime.datetime)
    idleThreshExceeded = QtC.Signal(datetime.datetime)
    sendImagePath = QtC.Signal(str)

    def __init__(self, daemonWidget=None, parent=None):
        super(ImageMonitorWorker, self).__init__(daemonWidget=daemonWidget, parent=parent)
        self.config = daemonWidget.mainWindow.config
        self.base_path = Path(self.config.IMAGE_MONITOR.BASE_PATH)
        self.idle_thresh = self.config.IMAGE_MONITOR.IDLE_THRESH
        self._running = False
        self._last_image_time = None
        self.observer = Observer()

    def run(self):
        self._check_or_create_dir()
        self._read_existing_files()
        self._start_monitor()

    def _check_or_create_dir(self):
        self.current_date = datetime.datetime.now().strftime('%Y_%m_%d')
        self.current_dir = self.base_path / self.current_date
        if not self.current_dir.exists():
            os.makedirs(self.current_dir)

    def _read_existing_files(self):
        self.existing_files = set(self.current_dir.glob('*.jpg'))

    def _start_monitor(self):
        event_handler = FileSystemEventHandler()
        event_handler.on_created = self._on_new_file
        self.observer.schedule(event_handler, self.current_dir, recursive=False)
        self.observer.start()

        self.idle_timer = QtC.QTimer()
        self.idle_timer.timeout.connect(self._check_idle)
        self.idle_timer.start(1000)

    def _on_new_file(self, event):
        if event.src_path.endswith('.jpg') and event.src_path not in self.existing_files:
            if not self._running:
                self.findNewImage.emit(datetime.datetime.now())
                self._running = True
            QtC.QThread.msleep(200)
            self.sendImagePath.emit(event.src_path)
            self._last_image_time = datetime.datetime.now()

    def _check_idle(self):
        if self._running and self._last_image_time and (datetime.datetime.now() - self._last_image_time).seconds > self.idle_thresh:
            self.idleThreshExceeded.emit(datetime.datetime.now())
            self._running = False

        if datetime.datetime.now().strftime('%Y_%m_%d') != self.current_date:
            self.observer.stop()
            self.observer.join()
            self._check_or_create_dir()
            self._read_existing_files()
            self._start_monitor()

    def stop(self):
        self.observer.stop()
        self.observer.join()
        self.idle_timer.stop()