from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from facade import Facade
import sys

import logging
logging.basicConfig(level=logging.INFO)


class MainWindow(QMainWindow):
    def __init__(self, facade):
        super().__init__()
        from PyQt5 import uic
        self.ui = uic.loadUi('forms/MainWindow.ui', self)
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.facade = facade
        logging.log(logging.INFO, 'Приложение запущено')


class Builder:
    def __init__(self):
        self.facade = None
        self.gui = None

    def create_facade(self):
        self.facade = Facade()

    def create_gui(self):
        if self.facade is not None:
            self.gui = MainWindow(self.facade)

    def get_result(self):
        if self.facade is not None and self.gui is not None:
            return self.gui


if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    builder = Builder()
    builder.create_facade()
    builder.create_gui()
    window = builder.get_result()
    window.show()
    qapp.exec()
