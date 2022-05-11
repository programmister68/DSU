from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractScrollArea, QTableWidgetItem, QMessageBox

from facade import Facade
import sys

import logging
logging.basicConfig(level=logging.INFO)


class MainWindow(QMainWindow):
    """
    Класс создания главного окна.
    """
    def __init__(self, facade):
        """
        Загрузка основного окна, прикрепление действий к кнопкам
        и отображение списка элементов СНМ в tableWidget.
        """
        super().__init__()
        self.list = []
        self.ui = uic.loadUi('forms/MainWindow.ui', self)
        self.setWindowIcon(QIcon('icons/study.ico'))
        self.facade = facade
        self.setWindowTitle('Disjoint-Set')
        self.tableWidget.insertRow(0)

        self.addButton.clicked.connect(self.make_set)
        self.unionButton.clicked.connect(self.union)
        self.findButton.clicked.connect(self.find)
        self.saveButton.clicked.connect(self.save)
        self.deleteButton.clicked.connect(self.delete_data)

        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["1"])
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.update()
        logging.log(logging.INFO, 'Приложение запущено')

    def update(self):
        """
        Функция обновления содержимого таблицы
        :return: None
        """
        self.tableWidget.removeRow(0)
        self.tableWidget.insertRow(0)
        list_set = self.facade.print_sets()
        counter = 0
        for i in list_set[0]:
            self.tableWidget.setColumnCount(counter + 1)
            self.tableWidget.setItem(0, counter, QTableWidgetItem(str(i)))
            counter += 1

    def make_set(self):
        """
        Функция добавления данных в структуру данных
        :return: None
        """
        text = self.lineAdd.text()
        self.facade.push(int(text))
        self.facade.make_set()
        self.update()

        logging.log(logging.INFO, 'Элемент добавлен.')

    def union(self):
        """
        Функция объединения двух элементов
        :return: None
        """
        self.ui = UnionWidget(self.facade, self)
        self.ui.show()
        logging.log(logging.INFO, 'Окно объединения запущено')

    def find(self):
        """
        Функция поиска представителя (родителя) введённого элемента
        :return: None
        """
        text = int(self.lineFind.text())
        if self.facade.find(int(text)) is False:
            self.warning_not_found()
            self.label.setText('Родитель не найден')
        else:
            self.label.setText(str(self.facade.find(int(text))))
            logging.log(logging.INFO, 'Родитель найден!')

    def save(self):
        """
        Функция сохранения данных в Базу Данных
        :return:
        """
        self.facade.saveDB()
        self.messageLine.setText('Данные сохранены!')
        logging.log(logging.INFO, 'Данные сохранены')

    def delete_data(self):
        """
        Функция удаления данных из Базы Данных
        :return:
        """
        self.facade.deleteDB()
        self.update()
        self.messageLine.setText('Данные удалены!')
        logging.log(logging.INFO, 'Данные удалены')

    def load(self):
        """
        Функция загрузки данных из Базы Данных
        :return:
        """
        self.facade.loadDB()
        self.update()
        logging.log(logging.INFO, 'Данные загружены')

    def warning_not_found(self):
        """
        Создание MessageBox, при отсутсвии элемента для поиска родителя.
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка")
        messagebox_del.setWindowIcon(QIcon('icons/warning.ico'))
        messagebox_del.setText("Данного элемента нет")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()


class UnionWidget(QtWidgets.QWidget):
    """
    Класс инициализации окна объединения множеств.
    """
    def __init__(self, facade, link=None):
        """
        Загрузка основного окна
        :param link: ссылка на родительское окно
        """
        super().__init__()
        self.facade = facade
        self.link = link
        self.ui = uic.loadUi('forms/dialog_union.ui', self)
        self.setWindowIcon(QIcon('icons/union.ico'))
        self.unionButton2.clicked.connect(self.union)
        self.setWindowTitle('Union')

    def union(self):
        """
        Функция объединения двух множеств
        :return: None
        """
        text = int(self.linePush_1st.text())
        text2 = int(self.linePush_2nd.text())

        for list_set in self.facade.print_sets():
            for num in list_set:
                if text == num:
                    for num2 in list_set:
                        if text2 == num2:
                            if text2 == text:
                                self.warning_num_already_union()
                            else:
                                self.facade.union(text, text2)
                                self.link.update()
                                logging.log(logging.INFO, 'Элементы объединены')
                                break
                            break
                    else:
                        self.warning_not_found()
                        break
                    break
            else:
                self.warning_not_found()
                break

    def warning_num_already_union(self):
        """
        Создание MessageBox, при вводе несуществующего в списке элемента для поиска
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка")
        messagebox_del.setWindowIcon(QIcon('icons/warning.ico'))
        messagebox_del.setText("Элементы уже объединёны")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()

    def warning_not_found(self):
        """
        Создание MessageBox, при вводе несуществующего в списке элемента (элементов) для объединения
        :return: None
        """
        messagebox_del = QMessageBox(self)
        messagebox_del.setWindowTitle("Ошибка")
        messagebox_del.setWindowIcon(QIcon('icons/warning.ico'))
        messagebox_del.setText("Данного элемента нет")
        messagebox_del.setIcon(QMessageBox.Warning)
        messagebox_del.setStandardButtons(QMessageBox.Ok)
        messagebox_del.show()


class Builder:
    """
    Класс паттерна "Строитель".
    Порождающий паттерн проектирования, который позволяет создавать сложные объекты пошагово.
    """
    def __init__(self):
        """
        Инициализация переменных facade и gui.
        """
        self.facade = None
        self.gui = None

    def create_facade(self):
        """
        Создание ссылки на объект фасада (Facade).
        :return: None
        """
        self.facade = Facade()

    def create_gui(self):
        """
        Создание ссылки на объект графики (MainWindow), если создана ссылка на фасад.
        :return: None
        """
        if self.facade is not None:
            self.gui = MainWindow(self.facade)

    def get_result(self):
        """
        Получение ссылки на объект графики (MainWindow).
        :return: gui - ссылка на объект графики.
        """
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
