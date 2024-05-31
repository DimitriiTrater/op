# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'films.ui'
##
## Created by: Qt User Interface Compiler version 5.15.14
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.films_table = QTableWidget(self.centralwidget)
        self.films_table.setObjectName(u"films_table")
        self.films_table.setGeometry(QRect(0, 0, 531, 561))
        self.edit_btn = QPushButton(self.centralwidget)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setGeometry(QRect(540, 100, 251, 51))
        self.new_btn = QPushButton(self.centralwidget)
        self.new_btn.setObjectName(u"new_btn")
        self.new_btn.setGeometry(QRect(540, 0, 251, 51))
        self.delete_btn = QPushButton(self.centralwidget)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setGeometry(QRect(540, 200, 251, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FILMS", None))
        self.edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.new_btn.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

