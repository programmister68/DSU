from PyQt5 import QtCore, QtGui, QtWidgets


class UiForm(object):
    def __init__(self):
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.labelDSU = QtWidgets.QLabel(Form)
        self.listWidgetDSU = QtWidgets.QListWidget(Form)
        self.lineAdd = QtWidgets.QLineEdit(Form)
        self.controlLayout = QtWidgets.QFormLayout()
        self.unionButton = QtWidgets.QPushButton(Form)
        self.addButton = QtWidgets.QPushButton(Form)
        self.lineUnion = QtWidgets.QLineEdit(Form)
        self.lineFind = QtWidgets.QLineEdit(Form)
        self.messageString = QtWidgets.QLabel(Form)
        self.findButton = QtWidgets.QPushButton(Form)

    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(846, 591)
        form.setMinimumSize(QtCore.QSize(761, 0))
        self.gridLayout.setObjectName("gridLayout")

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(39, 197, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 197, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelDSU.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Nokia Sans S60")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.labelDSU.setFont(font)
        self.labelDSU.setLineWidth(5)
        self.labelDSU.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDSU.setObjectName("labelDSU")
        self.gridLayout.addWidget(self.labelDSU, 0, 0, 1, 1)

        self.listWidgetDSU.setObjectName("listWidgetDSU")
        self.gridLayout.addWidget(self.listWidgetDSU, 1, 0, 1, 1)
        self.controlLayout.setObjectName("controlLayout")

        font = QtGui.QFont()
        font.setFamily("Nokia Sans S60")
        font.setPointSize(10)
        self.lineAdd.setFont(font)
        self.lineAdd.setObjectName("lineAdd")
        self.controlLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineAdd)

        self.addButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Nokia Sans S60")
        font.setPointSize(10)
        self.addButton.setFont(font)
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setObjectName("addButton")
        self.controlLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.addButton)

        self.unionButton.setMinimumSize(QtCore.QSize(0, 0))
        self.unionButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Nokia Sans S60")
        font.setPointSize(10)
        self.unionButton.setFont(font)
        self.unionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.unionButton.setObjectName("unionButton")
        self.controlLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.unionButton)

        font = QtGui.QFont()
        font.setFamily("Nokia Sans S60")
        font.setPointSize(10)
        self.lineUnion.setFont(font)
        self.lineUnion.setObjectName("lineUnion")
        self.controlLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineUnion)

        font = QtGui.QFont()
        font.setFamily("Nokia Sans S60")
        font.setPointSize(10)
        self.lineFind.setFont(font)
        self.lineFind.setObjectName("lineFind")
        self.controlLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineFind)

        self.messageString.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 60, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.messageString.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Nokia Sans S60")
        font.setPointSize(9)
        self.messageString.setFont(font)
        self.messageString.setText("")
        self.messageString.setObjectName("messageString")
        self.controlLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.messageString)

        font = QtGui.QFont()
        font.setFamily("Nokia Sans S60")
        font.setPointSize(10)
        self.findButton.setFont(font)
        self.findButton.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.findButton.setObjectName("findButton")
        self.controlLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.findButton)
        spacer_item = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controlLayout.setItem(10, QtWidgets.QFormLayout.FieldRole, spacer_item)
        self.gridLayout.addLayout(self.controlLayout, 1, 1, 2, 2)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Disjoint Set Union"))
        self.labelDSU.setText(_translate("Form", "Система непересекающихся множеств (DSU)"))
        self.addButton.setText(_translate("Form", "Добавить"))
        self.unionButton.setText(_translate("Form", "Обьединить"))
        self.findButton.setText(_translate("Form", "Найти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UiForm()
    ui.setup_ui(Form)
    Form.show()
    sys.exit(app.exec_())
