import sys
from unittest import TestCase

from PyQt5 import QtCore
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

from gui import MainWindow, UnionWidget
from facade import Facade


class FunctionalTest(TestCase):
    def setUp(self):
        self.qapp = QApplication(sys.argv)
        name = 'dsu_DB.db'
        self.facade = Facade(name)
        self.window = MainWindow(self.facade)
