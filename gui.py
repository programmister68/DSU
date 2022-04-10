from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QGraphicsScene, QMessageBox
from PyQt5 import uic
from facade import Facade
import sys
import logging

logging.basicConfig(level=logging.INFO)
# logging.disable(logging.INFO)


class MainWindow(QMainWindow):
    """
    этот класс создает главное окно
    """
    def __init__(self, facade):  # что такое *args, **kwargs??
        """
        здесь загружается основное окно, прикрепляются действия к кнопкам (вызов функций) и отрисовывается дерево
        :param facade: ссылка на фасад
        """
        self.facade = facade
        super().__init__()
        self.ui = uic.loadUi("forms/dsu_interface.ui", self)
        self.window().setWindowTitle(
            "Реализация и моделирование структуры данных словарь на основе двоичного дерева поиска. Илюхин")
        self.scene = QGraphicsScene(0, 0, 800, 600)
        self.ui.canvas.setScene(self.scene)

    def closeEvent(self, event):
        """
        Действия при закрытии основного окна (нажатие на крестик).
        Если есть несохраненные данные, то появится окно с вопросом о сохранении данных ("Хотите их сохранить?")
        :param event: ососбое действие
        :return: None
        """
        if self.facade.data_wait_for_save:
            logging.log(logging.INFO, ' есть несохраненные данные')
            self.save.setWindowTitle("Несохраненные данные")
            self.save.setText("Остались несохраненные данные!")
            self.save.setInformativeText("Хотите их сохранить?")

            self.save.setIcon(QMessageBox.Question)
            self.save.setStandardButtons(QMessageBox.Cancel | QMessageBox.Save)

            self.save.buttonClicked.connect(self.action)
            self.save.exec_()
        else:
            logging.log(logging.INFO, ' несохраненных данных нет')

        logging.log(logging.INFO, ' окно закрыто')

    def action(self, btn):
        """
        действия при нажатии на кнопки всплывабщего окна при закрытии основного окна.
        при нажати на кнопку save - вызов save_data (сохранение данных в БД)
        :param btn: нажатая кнопка
        :return: None
        """
        if btn.text() == "Save":
            logging.log(logging.INFO, " данные сохранены")
            self.facade.save_data()
        else:
            logging.log(logging.INFO, " данные не сохранены")

    def open_dialog_input(self):
        """
        функция для открытия диалогового окна ввода данных и установки заголовка окна
        :return: NONE
        """
        dialog = DialogInput(self.facade, self)
        dialog.setWindowTitle("Добавление данных")
        dialog.show()

    def open_dialog_delete(self):
        """
        функция для открытия диалогового окна удаления данных и установки заголовка окна
        :return: NONE
        """
        dialog = DialogDelete(self.facade, self)  # тут self. нужен для теста (чтобы можно было обратиться к dialog)
        dialog.setWindowTitle("Удаление данных")
        dialog.show()

    def open_dialog_search(self):
        """
        функция для открытия диалогового окна поиска данных и установки заголовка окна
        :return: NONE
        """
        dialog = DialogSearch(self.facade, self)
        dialog.setWindowTitle("Поиск элемента")
        dialog.show()

    def draw_el(self, x, y, key, data, left=None, height=0):
        """
        отрисовка круга, текса (key, data) и линии (ветки)
        :param x: кардината отрисовки элементов
        :param y: кардината отрисовки элементов
        :param key: ключ, который нужно вывести
        :param data: данные, которые нужно вывести
        :param left: левый это или правый элемнта в дереве (для отрисовки линии - ветки)
        :param height: высота ветки (если бы это был прямой треугольник)
        :return: None
        """
        self.scene.addEllipse(x, y, 40, 40)

        long = len(str(key))
        text = self.scene.addText(f"{key}")
        text.moveBy(x + 17 - long * 3, y + 10)

        long = len(str(data))
        text = self.scene.addText(f"{data}")
        text.moveBy(x + 17 - long * 3, y + 40)

        if left == 1:
            self.scene.addLine(x + 30, y - 10, x + self.branch_len + 15, y - height + 60)
        if left == 0:
            self.scene.addLine(x + 10, y - 10, x - self.branch_len + 25, y - height + 60)

    def draw_tree(self):
        """
        Расчет координат элементов и передача их в draw_el
        :return: None
        """
        self.scene.clear()
        path = self.facade.bypass_tree()

        x = 50 * (2 ** path[0]) + 50
        y = 150
        h = 50
        height = h * path[0] + h  # высота ветки (если бы это был прямой треугольник)
        self.branch_len = (x - 50) // 2  # ширина ветки (если бы это был прямой треугольник)
        layer = 0  # слой дерева
        frame_x = 0
        for val in range(1, path[0] + 2):
            frame_x += h * val

        self.scene = QGraphicsScene(0, 0, x * 2 + 100, frame_x + 300)
        logging.log(logging.INFO, f' размер холста - {x * 2 + 100}, {y * path[0] + 100}')
        self.ui.canvas.setScene(self.scene)

        if len(path) != 1:
            self.draw_el(x, y, path[1][0], path[1][1])

        for n in range(2, len(path)):
            if path[n][1] is not None:
                y += height
                layer += 1

                if path[n - 1][0] > path[n][0]:  # значит этот элемент левее --> вычитаем
                    x -= self.branch_len
                    self.draw_el(x, y, path[n][0], path[n][1], 1, height)

                else:  # значит этот элемент правее --> прибавляем
                    x += self.branch_len
                    self.draw_el(x, y, path[n][0], path[n][1], 0, height)
                self.branch_len //= 2

                height -= h

            else:  # возвращаемся назад
                height += h
                layer -= 1
                y -= height
                self.branch_len *= 2
                if path[n - 1][0] < path[n][0]:
                    x += self.branch_len
                else:
                    x -= self.branch_len


class DialogSearch(QDialog):
    """
    класс для инициализации диалогового окна поиска данных
    """

    def __init__(self, facade, parent=None):
        """
        здесь загружается диалоговое окно поиска элемента и прописываются действия при нажатии на кнопку (вызов функции)
        :param facade: ссылка на объект класса Facade
        :param parent: ссылка на родительское окно
        """
        super(DialogSearch, self).__init__(parent)
        self.facade = facade
        self.ui = uic.loadUi("forms/search.ui", self)
        self.ui.btn_find.clicked.connect(self.search)

    def search(self):
        """
        Осуществляется поиск по введенному элементу.
        Если он существует выведит Данный элемент есть в дереве.
        А если не существует - Данного элемента нет в дереве.
        :return: None
        """
        link = self.facade.search_element_in_tree(int(self.ui.input_key.text()))
        if link is not None:
            self.ui.label_info.setText(f"Данный элемент есть в дереве: {self.ui.input_key.text()}, {link.data}")
        else:
            self.ui.label_info.setText(f"Данного элемента нет в дереве.")


class DialogDelete(QDialog):
    """
    класс для инициализации диалогового окна удаления данных
    """

    def __init__(self, facade, parent=None):
        """
        здесь загружается диалоговое окно удаления данных и прописываются действия при нажатии на кнопки (вызов функций)
        :param facade: ссылка на объект класса Facade
        :param parent: ссылка на родительское окно
        """
        super(DialogDelete, self).__init__(parent)
        self.facade = facade
        self.ui = uic.loadUi("forms/delete.ui", self)
        self.ui.btn_remove.clicked.connect(self.delete)
        self.ui.btn_remove_all.clicked.connect(lambda: self.del_all())

    def del_all(self):
        """
        Создание messagebox при нажатии кнопки "удалить все"
        :return: None
        """
        if self.facade.dictionary.key is not None:  # если есть данные для удаления
            self.messagebox_del_all = QMessageBox(self)
            self.messagebox_del_all.setWindowTitle("Удаление данных")
            self.messagebox_del_all.setText("Вы уверены, что хотите удалить все данные?")
            self.messagebox_del_all.setInformativeText("После сохранения данные будут утеряны!")

            self.messagebox_del_all.setIcon(QMessageBox.Question)
            self.messagebox_del_all.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)

            self.messagebox_del_all.buttonClicked.connect(self.action)
            self.messagebox_del_all.show()
        else:
            QMessageBox.warning(self, 'Удаление данных', "Данных для удаления нет", QMessageBox.Ok)

    def action(self, button):
        """
        При нажатии Ok в messagebox_del_all.
        Удаление данных из структуры данных.
        :param button: нажатая кнопка в messagebox_del_all
        :return: None
        """
        if button.text() == "OK":
            self.facade.del_all_from_bst()
            self.parent().draw_tree()
            logging.log(logging.INFO, 'данные удалены')
        else:
            logging.log(logging.INFO, 'данные не удалены')

    def delete(self):
        """
        действия при нажатии кнопки "Удалить".
        Удаляет элемент из структуры данных, если он существует
        :return: None
        """
        link = self.facade.search_element_in_tree(self.ui.input_key.value())  # ссылка на элемент, который удаляем
        if link is not None:
            try:
                self.ui.label_info.setText(f"Вы удалили: {self.ui.input_key.value()}, {link.data}")
                self.facade.delete_value(self.ui.input_key.value())
                self.parent().draw_tree()
            except RecursionError:
                self.ui.label_info.setText(f"Дерево слишком высокое!\nПопробуйте ввести ключ для другого поддерева.")
        else:
            self.ui.label_info.setText(f"Данного ключа не существует!")


class DialogInput(QDialog):
    """
    класс для инициализации диалогового окна ввода данных
    """

    def __init__(self, facade, parent=None):
        """
        здесь загружается основное окно и прописываются действия при нажатии на кнопку (вызов функций)
        :param facade: ссылка на объект класса Facade
        :param parent: ссылка на родительское окно
        """
        self.facade = facade
        super(DialogInput, self).__init__(parent)
        self.ui = uic.loadUi("forms/input.ui", self)
        self.ui.btn_insert.clicked.connect(self.add)

    def add(self):
        """
        действия при нажатии кнопки "Сохранить".
        Добавляет элемент в структуру данных, если он не существует
        :return: None
        """
        if self.ui.data_input.text() != '' and self.facade.search_element_in_tree(self.ui.key_input.value()) is None:
            try:
                self.facade.insert_value(self.ui.key_input.value(), self.ui.data_input.text())
                self.ui.label_info.setText(f"Вы ввели: {self.ui.key_input.value()}, {self.ui.data_input.text()}")
                self.parent().draw_tree()
                logging.log(logging.INFO, 'заполните поля')
            except RecursionError:

                self.ui.label_info.setText(f"Дерево слишком высокое!\nПопробуйте ввести ключ для другого поддерева.")

        elif self.ui.data_input.text() == '':
            self.ui.label_info.setText(f"Заполните поле!")
            logging.log(logging.INFO, 'заполните поля')

        else:
            self.ui.label_info.setText(f"Данный ключ уже существует!")


class Builder:
    """
    Паттерн строитель.
    Это порождающий паттерн проектирования, который позволяет создавать сложные объекты пошагово.
    """

    def __init__(self):
        """
        объявление переменных facade и gui
        """
        self.facade = None
        self.gui = None

    def create_facade(self):
        """
        создание ссылки на объект фасада (Facade)
        :return: None
        """
        self.facade = Facade()

    def create_gui(self):
        """
        создание ссылки на объект графики (MainWindow), если создана ссылка на фасад
        :return: None
        """
        if self.facade is not None:
            self.gui = MainWindow(self.facade)

    def get_result(self):
        """
        получение ссылки на объект графики (MainWindow)
        :return: gui - ссылка на объект графики
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