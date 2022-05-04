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
        name = 'dsu_test_DB.db'
        self.facade = Facade(name)
        self.window = MainWindow(self.facade)

    def test_elem_add(self):
        add_Button = self.window.ui.addButton
        self.window.lineAdd.setValue(1)
        QTest.mouseClick(add_Button, QtCore.Qt.MouseButton.LeftButton)
        self.window.lineAdd.setValue(12)
        QTest.mouseClick(add_Button, QtCore.Qt.MouseButton.LeftButton)

    def test_elem_union(self):
        add_Button = self.window.ui.addButton
        self.window.lineAdd.setValue(1)
        QTest.mouseClick(add_Button, QtCore.Qt.MouseButton.LeftButton)
        self.window.lineAdd.setValue(12)
        QTest.mouseClick(add_Button, QtCore.Qt.MouseButton.LeftButton)

        union_Button = self.window.ui.unionButton
        QTest.mouseClick(union_Button, QtCore.Qt.MouseButton.LeftButton)
        for window in self.qapp.topLevelWidgets():
            if isinstance(window, UnionWidget):
                dialog = window
                break
        else:
            self.fail()

        dialog.linePush_1st.setValue(1)
        dialog.linePush_2nd.setValue(12)
        QTest.mouseClick(dialog.unionButton2, QtCore.Qt.MouseButton.LeftButton)

    def test_elem_find(self):
        add_Button = self.window.ui.addButton
        self.window.lineAdd.setValue(1)
        QTest.mouseClick(add_Button, QtCore.Qt.MouseButton.LeftButton)
        self.window.lineAdd.setValue(12)
        QTest.mouseClick(add_Button, QtCore.Qt.MouseButton.LeftButton)

        find_Button = self.window.ui.findButton
        self.window.lineFind.setValue(1)
        QTest.mouseClick(find_Button, QtCore.Qt.MouseButton.LeftButton)

    def test_save(self):
        add_Button = self.window.ui.addButton
        self.window.lineAdd.setValue(1)
        QTest.mouseClick(add_Button, QtCore.Qt.MouseButton.LeftButton)
        self.window.lineAdd.setValue(12)
        QTest.mouseClick(add_Button, QtCore.Qt.MouseButton.LeftButton)

        save_Button = self.window.ui.saveButton
        QTest.mouseClick(save_Button, QtCore.Qt.MouseButton.LeftButton)

    def test_sets_delete(self):
        delete_Button = self.window.ui.deleteButton
        QTest.mouseClick(delete_Button, QtCore.Qt.MouseButton.LeftButton)
