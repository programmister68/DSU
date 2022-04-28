from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QAbstractScrollArea, QTableWidgetItem

from facade import Facade
import sys

import logging
logging.basicConfig(level=logging.INFO)


class MainWindow(QMainWindow):
    def __init__(self, facade):
        super().__init__()
        self.list = []
        self.ui = uic.loadUi('forms/MainWindow.ui', self)
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.facade = facade
        self.setWindowTitle('Disjoint-Set')
        self.tableWidget.insertRow(0)

        self.addButton.clicked.connect(self.make_set)
        self.unionButton.clicked.connect(self.union)
        self.findButton.clicked.connect(self.find)
        self.saveButton.clicked.connect(self.save)
        self.deleteButton.clicked.connect(self.delete_data)
        self.loadButton.clicked.connect(self.load)

        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["1"])
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.update()
        logging.log(logging.INFO, 'Приложение запущено')

    def update(self):
        self.tableWidget.removeRow(0)
        self.tableWidget.insertRow(0)
        list_set = self.facade.print_sets()
        counter = 0
        for i in list_set[0]:
            self.tableWidget.setColumnCount(counter + 1)
            self.tableWidget.setItem(0, counter, QTableWidgetItem(str(i)))
            counter += 1

    def make_set(self):  # Кнопка добавления данных
        text = self.lineAdd.text()
        self.facade.push(int(text))
        self.facade.make_set()
        self.update()

        logging.log(logging.INFO, 'Элемент добавлен.')

    def union(self):  # Кнопка объединения двух элементов
        pass
        self.ui = UnionWidget(self.facade, self)
        self.ui.show()
        logging.log(logging.INFO, 'Окно объединения запущено')

    def find(self):  # Кнопка поиска родителя
        text = self.lineFind.text()
        self.label.setText(str(self.facade.find(int(text))))
        logging.log(logging.INFO, 'Родитель найден!')

    def save(self):  # Кнопка сохранения данных в БД
        self.facade.saveDB()
        logging.log(logging.INFO, 'Данные сохранены')

    def delete_data(self):  # Кнопка удаления данных из БД
        self.facade.deleteDB()
        self.update()
        logging.log(logging.INFO, 'Данные удалены')

    def load(self):  # Кнопка загрузки данных из БД
        self.facade.loadDB()
        self.update()
        logging.log(logging.INFO, 'Данные загружены')

    def build(self, data):
        # print(self.facade.get)
        # self.WidgetDSU.addItems(self.list)
        pass


class UnionWidget(QtWidgets.QWidget):
    def __init__(self, facade, link=None):
        super().__init__()
        self.facade = facade
        self.link = link
        self.ui = uic.loadUi('forms/dialog_union.ui', self)
        self.setWindowIcon(QIcon('icons/union.ico'))
        self.unionButton.clicked.connect(self.union)
        self.setWindowTitle('Union')

    def union(self):  # Кнопка объединения двух элементов
        text = self.linePush_1st.text()
        text2 = self.linePush_2nd.text()
        self.facade.union(int(text),int(text2))
        window.update()

        logging.log(logging.INFO, 'Элементы объединены')


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
    logging.log(logging.INFO, 'Приложение завершило свою работу.')
