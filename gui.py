from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

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

        self.addButton.clicked.connect(self.make_set)
        self.unionButton.clicked.connect(self.union)
        self.findButton.clicked.connect(self.find)
        self.saveButton.clicked.connect(self.save)
        self.deleteButton.clicked.connect(self.delete)
        self.loadButton.clicked.connect(self.load)

        logging.log(logging.INFO, 'Приложение запущено')

    def make_set(self):  # Кнопка добавления данных
        # print('+')
        # data = int(self.lineAdd.text())
        # print('+')
        #
        # self.facade.push(data)
        # # print('+')
        # data = str(data)
        # self.build(data)
        # print('+-')
        pass

        logging.log(logging.INFO, 'Элемент добавлен.')

    def union(self):  # Кнопка объединения двух элементов
        pass
        self.ui = UnionWidget(self.facade, self)
        self.ui.show()
        logging.log(logging.INFO, 'Окно объединения запущено')

    def find(self):  # Кнопка поиска родителя
        pass

        logging.log(logging.INFO, 'Пусть мама услышит, пусть мама придёт... Родитель найден!')

    def save(self):  # Кнопка сохранения данных в БД
        pass

        logging.log(logging.INFO, 'Данные сохранены')

    def delete(self):  # Кнопка удаления данных из БД
        pass

        logging.log(logging.INFO, 'Данные удалены')

    def load(self):  # Кнопка загрузки данных из БД
        pass

        logging.log(logging.INFO, 'Данные загружены')

    def build(self, data):
        print(self.facade.get)
        self.WidgetDSU.addItems(self.list)

    def warning_no_int(self):
        """
        Создание MessageBox, если данные содержат буквы и символы.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Введите число!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)

        messagebox_del.show()
        logging.log(logging.INFO, 'Открыто диалоговое окно "Ошибка ввода"')

    def warning_no_nums(self):
        """
        Создание MessageBox, если данные не введены.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Заполните поле!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)

        messagebox_del.show()
        logging.log(logging.INFO, 'Открыто диалоговое окно "Ошибка ввода"')


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
        pass

        logging.log(logging.INFO, 'Элементы объединены')

    def warning_no_int(self):
        """
        Создание MessageBox, если данные содержат буквы и символы.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Введите число!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)

        messagebox_del.show()
        logging.log(logging.INFO, 'Открыто диалоговое окно "Ошибка ввода"')

    def warning_no_nums(self):
        """
        Создание MessageBox, если данные не введены.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка ввода")
        messagebox_del.setText("Заполните поле!")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)

        messagebox_del.show()
        logging.log(logging.INFO, 'Открыто диалоговое окно "Ошибка ввода"')


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
