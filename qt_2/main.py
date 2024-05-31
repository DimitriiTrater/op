from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QPushButton,
    QListWidgetItem,
    QTextEdit,
)

from config import SIZE

import PyQt5.QtCore
import requests
import sys
import logging
import re
import threading


class App(QWidget):
    def __init__(self) -> None:
        logger.info("App constructor")
        super().__init__()
        self.setFixedSize(SIZE["H"], SIZE["W"])

        label = QLabel(text="City Name")
        self.text = QLineEdit("Бобруйск")

        okButton = QPushButton("OK")
        okButton.clicked.connect(self.get_request)

        nameCityBox = QHBoxLayout()
        nameCityBox.addWidget(label)
        nameCityBox.addWidget(self.text)
        nameCityBox.addWidget(okButton)

        self.branches = {}

        listBox = QHBoxLayout()
        self.list = QListWidget()
        self.list.itemClicked.connect(self.show_info)
        self.list.itemClicked.connect(self.show_address)
        self.list.itemClicked.connect(self.show_work_time)
        listBox.addWidget(self.list)

        addressAndWorkTimeBox = QVBoxLayout()

        self.address = QLabel("Address:")
        addressAndWorkTimeBox.addWidget(self.address)
        self.address.setFixedSize(450, 200)
        self.address.setMargin(25)

        self.workTime = QLabel("Work Time:")
        addressAndWorkTimeBox.addWidget(self.workTime)
        self.workTime.setFixedSize(450, 400)
        self.workTime.setMargin(25)

        listBox.addLayout(addressAndWorkTimeBox)

        self.currencies = QTextEdit()
        listBox.addWidget(self.currencies)

        mainBox = QVBoxLayout()
        mainBox.addLayout(nameCityBox)
        mainBox.addLayout(listBox)

        self.setLayout(mainBox)
        self.show()

    def show_info(self, item):
        logger.info("show_info")
        info = item.text()
        logger.debug(info)
        branch = self.branches[info]
        currencies = [ "USD", "EUR", "RUB"
                     , "GBP", "CAD", "PLN"
                     , "SEK", "CHF", "JPY"
                     , "CNY", "CZK", "NOK"
                     ]

        text = ""
        for currency in currencies:
            _in = branch[f"{currency}_in"]
            _out = branch[f"{currency}_out"]
            if _in != "0.0000":
                text += f"{currency}\nПокупка: {_in}\nПродажа: {_out}\n\n"
        self.currencies.setText(text)



    def show_address(self, item):
        logger.info("show_address")
        self.address.clear()
        logger.debug(f"{item.text()}")
        logger.debug(f"{self.branches[item.text()]}")
        branch = self.branches[item.text()]
        text = (
            f"Адрес: {branch['street_type']} {branch['street']}," +
            f"{branch['home_number']}"
        )
        self.address.setText(text)

    def show_work_time(self, item):
        logger.info("show_work_time")
        self.workTime.clear()
        branch = self.branches[item.text()]
        worktime = branch["info_worktime"].split("|")
        text = "График работы:\n"
        valuesForColon = [2, 5, 11, 17, 23]
        valuesForDash = [8, 20]
        for i in range(len(worktime)-1):
            res = ""
            for j in range(len(worktime[i])):
                if j in valuesForColon:
                    res += ":" + (" " if j == 2 else "")
                    continue
                if j in valuesForDash:
                    res += " - "
                    continue
                if j == 14:
                    res += "(пер. "
                    continue
                res += worktime[i][j]
            text += f"{res})\n"
        self.workTime.setText(text[:-1])

    def get_request(self) -> None:
        self.list.clear()

        if self.text.text() == "": ...

        data = requests.get(
            f"https://belarusbank.by/api/kursExchange?city={self.text.text()}"
        ).json()

        for item in data:
            branch_name = f"{item['filials_text']}"
            self.list.addItem(branch_name)
            self.branches[branch_name] = item
        logger.info("End of request")


    def keyPressEvent(self, e) -> None:
        logger.debug(f"Key event")
        if e.key() == PyQt5.QtCore.Qt.Key_Escape:
            self.close()
            logger.info("Escape from programm")
        if e.key() == PyQt5.QtCore.Qt.Key_Return:
            self.get_request()
            logger.info("Get request")
        logger.info


def main() -> None:
    logger.debug("Start programm")
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def logger_start() -> logging.Logger:
    FORMAT = "[ %(levelname)s::%(filename)s::%(lineno)s - %(funcName)10s() ] %(message)s"
    logging.basicConfig(format=FORMAT)
    t_logger = logging.getLogger(__name__)
    t_logger.setLevel(logging.DEBUG)
    return t_logger


if __name__ == "__main__":
    logger = logger_start()
    main()
