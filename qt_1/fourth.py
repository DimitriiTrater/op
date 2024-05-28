import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QPlainTextEdit,
    QCheckBox
)

import PyQt5.QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Заказ во \"Вкусно и точка\"")

        layout1 = QVBoxLayout()

        self.checkbox1 = QCheckBox("Чизбургер")
        self.checkbox2 = QCheckBox("Гамбургер")
        self.checkbox3 = QCheckBox("Кока-кола")
        self.checkbox4 = QCheckBox("Наггетсы")

        layout1.addWidget(self.checkbox1)
        layout1.addWidget(self.checkbox2)
        layout1.addWidget(self.checkbox3)
        layout1.addWidget(self.checkbox4)

        self.button = QPushButton("Заказать")
        self.button.setFixedSize(100, 30)
        self.button.clicked.connect(self.clicked)

        layout1.addWidget(self.button)

        self.orderInfo = QPlainTextEdit()
        self.orderInfo.setDisabled(True)
        layout1.addWidget(self.orderInfo)


        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

    def clicked(self):
        if self.checkbox1.isEnabled():
            self.orderInfo.insertPlainText("Чизбургер \n")
        if self.checkbox2.isEnabled():
            self.orderInfo.insertPlainText("Гамбургер \n")
        if self.checkbox3.isEnabled():
            self.orderInfo.insertPlainText("Кока-кола \n")
        if self.checkbox4.isEnabled():
            self.orderInfo.insertPlainText("Наггетсы \n")

    def keyPressEvent(self, e) -> None:
        if e.key() == PyQt5.QtCore.Qt.Key_Escape:
            self.close()
        if e.key() == PyQt5.QtCore.Qt.Key_Return:
            self.clicked()


def main() -> None:
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()
