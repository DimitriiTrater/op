from PyQt5.QtWidgets import (
    QWidget,
)


from editor_ui import Ui_EditWin
from db_worker import FilmsDBWorker
from film import Film

gl_genres : dict[str, int] = {}

class Editor(QWidget):
    def __init__(self, genres, ID=None):
        super().__init__()
        ui = Ui_EditWin()
        ui.setupUi(self)
        self.ID = ID
        self.rebuild_callback = None

        self.name = ui.name_of_film
        self.date = ui.date_of_film
        self.time = ui.time_of_film

        self.genres = ui.genre_of_film
        print(genres)
        for i in genres:
            gl_genres[i[1]] = i[0]

        print(gl_genres)
        for k, v in gl_genres.items():
            self.genres.addItem(k)

        self.show()

    def start_fn(self, fn):
        fn()

    def accept(self):
        self.rebuild_callback()
        if self.ID is None:
            FilmsDBWorker().add_film_in_db(
                Film(
                    name=str(self.name.toPlainText()),
                    date=int(self.date.text()),
                    time=int(str(self.time.toPlainText())),
                    genre=gl_genres[self.genres.currentText()]
                )
            )
        else:
            FilmsDBWorker().edit_film(
                Film(
                    name=str(self.name.toPlainText()),
                    date=int(self.date.text()),
                    time=int(str(self.time.toPlainText())),
                    genre=gl_genres[self.genres.currentText()]
                ),
                ID=self.ID
            )
        self.close()

    def reject(self):
        self.close()
