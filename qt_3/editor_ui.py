# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.14
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_EditWin(object):
    def setupUi(self, EditWin):
        if not EditWin.objectName():
            EditWin.setObjectName(u"EditWin")
        EditWin.resize(568, 179)
        self.buttonBox = QDialogButtonBox(EditWin)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 140, 531, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(EditWin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 91, 18))
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label_2 = QLabel(EditWin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 10, 91, 18))
        self.label_2.setFont(font)
        self.label_3 = QLabel(EditWin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 10, 101, 18))
        self.label_3.setFont(font)
        self.label_4 = QLabel(EditWin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(470, 10, 51, 18))
        self.label_4.setFont(font)
        self.name_of_film = QTextEdit(EditWin)
        self.name_of_film.setObjectName(u"name_of_film")
        self.name_of_film.setGeometry(QRect(40, 50, 91, 101))
        self.date_of_film = QDateEdit(EditWin)
        self.date_of_film.setObjectName(u"date_of_film")
        self.date_of_film.setGeometry(QRect(170, 50, 110, 32))
        self.genre_of_film = QComboBox(EditWin)
        self.genre_of_film.setObjectName(u"genre_of_film")
        self.genre_of_film.setGeometry(QRect(460, 50, 87, 32))
        self.time_of_film = QTextEdit(EditWin)
        self.time_of_film.setObjectName(u"time_of_film")
        self.time_of_film.setGeometry(QRect(310, 50, 121, 31))

        self.retranslateUi(EditWin)
        self.buttonBox.accepted.connect(EditWin.accept)
        self.buttonBox.rejected.connect(EditWin.reject)

        QMetaObject.connectSlotsByName(EditWin)
    # setupUi

    def retranslateUi(self, EditWin):
        EditWin.setWindowTitle(QCoreApplication.translate("EditWin", u"Editor", None))
        self.label.setText(QCoreApplication.translate("EditWin", u"Film name:", None))
        self.label_2.setText(QCoreApplication.translate("EditWin", u"Date:", None))
        self.label_3.setText(QCoreApplication.translate("EditWin", u"Time of film:", None))
        self.label_4.setText(QCoreApplication.translate("EditWin", u"Genre:", None))
        self.date_of_film.setDisplayFormat(QCoreApplication.translate("EditWin", u"yyyy", None))
    # retranslateUi

