from PyQt5 import uic, QtWidgets, QtCore, QtGui

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QTableWidgetItem,
    QAbstractItemView,
)

from datetime import date

from films_ui import Ui_MainWindow
from db_worker import FilmsDBWorker
from editor import Editor, gl_genres

import sys

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)

        self.e = None

        self.films_table = ui.films_table
        self.worker = FilmsDBWorker()
        self.fill_films_table()
        self.films_table.setHorizontalHeaderLabels(
            ["Название", "Год выпуска", "Длительность", "Жанр"])
        self.films_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.films_table.itemDoubleClicked.connect(self.edit_film)

        self.new_btn = ui.new_btn
        self.new_btn.clicked.connect(self.new_film)

        self.edit_btn = ui.edit_btn
        self.edit_btn.clicked.connect(self.edit_film)

        self.delete_btn = ui.delete_btn
        self.delete_btn.clicked.connect(self.delete_row)

        self.show()

    def new_film(self):
        self.e = Editor(self.worker.get_genres())
        self.e.start_fn(self.update_t)
        self.e.rebuild_callback = self.update

    def edit_film(self):
        row = self.films_table.currentRow()
        self.e = Editor(self.worker.get_genres(), self.films_table.item(row, 0).data(QtCore.Qt.UserRole))
        self.e.ID = self.films_table.item(row, 0).data(QtCore.Qt.UserRole)
        self.e.start_fn(self.update_t)
        self.e.rebuild_callback = self.update_t
        self.e.name.setText(self.films_table.item(row, 0).text())
        self.e.date.setDate(
            QtCore.QDate.fromString(
                self.films_table.item(row, 1).text(),
                "yyyy"
            )
        )
        self.e.time.setText(self.films_table.item(row, 2).text())
        self.e.genres.setCurrentIndex(gl_genres[self.films_table.item(row, 3).text()] - 1)

    def delete_row(self):
        row = self.films_table.currentRow()
        self.worker.delete_from_db_by_id(self.films_table.item(row, 0).data(QtCore.Qt.UserRole))
        self.films_table.removeRow(row)

    def update_t(self):
        self.films_table.clear()
        self.films_table.setRowCount(0)
        self.fill_films_table()

    def fill_films_table(self):
        rows = self.worker.get_info_from_db()
        if rows:
            self.films_table.setRowCount(len(rows))
            self.films_table.setColumnCount(len(rows[0]) - 1)
            for row_k, row_v in enumerate(rows):
                for col_k, col_v in enumerate(row_v[1:]):
                    item = QTableWidgetItem(str(col_v))
                    item.setData(QtCore.Qt.UserRole, row_v[0])
                    self.films_table.setItem(row_k, col_k, item)
        else:
            raise ValueError("Cant get rows")

    def clear(self):
        self.films_table.setRowCount(0)

def main() -> int:
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    return 0


if __name__ == "__main__":
    main()
