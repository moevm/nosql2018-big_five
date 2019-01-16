# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(150, 0, 511, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(17)
        self.label1.setFont(font)
        self.label1.setStyleSheet("label1")
        self.label1.setObjectName("label1")
        self.label1_2 = QtWidgets.QLabel(Form)
        self.label1_2.setGeometry(QtCore.QRect(200, 30, 511, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(13)
        self.label1_2.setFont(font)
        self.label1_2.setStyleSheet("label1")
        self.label1_2.setObjectName("label1_2")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(15, 70, 766, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label1.setText(_translate("Form", "  Анализ тестов BigFive"))
        self.label1_2.setText(_translate("Form", "Таблица с результатами"))

