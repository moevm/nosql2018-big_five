# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glv.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.importButton = QtWidgets.QPushButton(self.centralwidget)
        self.importButton.setGeometry(QtCore.QRect(270, 70, 251, 71))
        self.importButton.setObjectName("importButton")
        self.tablButton = QtWidgets.QPushButton(self.centralwidget)
        self.tablButton.setGeometry(QtCore.QRect(270, 190, 251, 71))
        self.tablButton.setObjectName("tablButton")
        self.analizButton = QtWidgets.QPushButton(self.centralwidget)
        self.analizButton.setGeometry(QtCore.QRect(270, 310, 251, 71))
        self.analizButton.setObjectName("analizButton")
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportButton.setGeometry(QtCore.QRect(270, 430, 251, 71))
        self.exportButton.setObjectName("exportButton")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(210, 10, 411, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(17)
        self.label1.setFont(font)
        self.label1.setStyleSheet("label1")
        self.label1.setObjectName("label1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.importButton.setText(_translate("MainWindow", "Импорт данных"))
        self.tablButton.setText(_translate("MainWindow", "Таблица данных"))
        self.analizButton.setText(_translate("MainWindow", "Анализ данных"))
        self.exportButton.setText(_translate("MainWindow", "Экспорт данных"))
        self.label1.setText(_translate("MainWindow", "  Анализ тестов BigFive"))

