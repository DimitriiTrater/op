import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QLCDNumber,
    QLabel
)

import PyQt5.QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Calc")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout4 = QVBoxLayout()

        firstTextboxLabel = QLabel("Первое число (целое): ")
        secondTextboxLabel = QLabel("Второе число (целое): ")

        self.textbox1 = QLineEdit()
        self.textbox2 = QLineEdit()

        layout2.addWidget(firstTextboxLabel)
        layout2.addWidget(self.textbox1)
        layout2.addWidget(secondTextboxLabel)
        layout2.addWidget(self.textbox2)

        layout1.addLayout(layout2)

        self.button = QPushButton("->")
        self.button.clicked.connect(self.clicked)

        layout1.addWidget(self.button)

        sumLabel = QLabel("Сумма: ")
        diffLabel = QLabel("Разность: ")
        multLabel = QLabel("Произведение: ")
        divLabel = QLabel("Деление: ")

        layout3.addWidget(sumLabel)
        layout3.addWidget(diffLabel)
        layout3.addWidget(multLabel)
        layout3.addWidget(divLabel)

        layout1.addLayout(layout3)

        self.lcd1 = QLCDNumber()
        self.lcd2 = QLCDNumber()
        self.lcd3 = QLCDNumber()
        self.lcd4 = QLCDNumber()

        layout4.addWidget(self.lcd1)

        layout4.addWidget(self.lcd2)
        layout4.addWidget(self.lcd3)
        layout4.addWidget(self.lcd4)

        layout1.addLayout(layout4)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

    def clicked(self):
        try:
            self.button.setText("->")
            self.lcd4.display(
                str(int(self.textbox1.text()) / int(self.textbox2.text())))
            self.lcd1.display(
                str(int(self.textbox1.text()) + int(self.textbox2.text())))
            self.lcd2.display(
                str(int(self.textbox1.text()) - int(self.textbox2.text())))
            self.lcd3.display(str(int(self.textbox1.text())
                              * int(self.textbox2.text())))
        except ZeroDivisionError:
            self.button.setText("ERROR")
            self.lcd4.display("ERROR")
            self.lcd1.display("ERROR")
            self.lcd2.display("ERROR")
            self.lcd3.display("ERROR")

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
