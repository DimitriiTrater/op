from film import Film

import sqlite3

class DBWorker:
    def __init__(self, db_name) -> None:
        self.__db_name = db_name
        self._connect_to_db()

    def __del__(self) -> None:
        self._close_db_connection()

    def _connect_to_db(self) -> None:
        self._connector = sqlite3.connect(self.__db_name)

    def _close_db_connection(self) -> None:
        self._connector.close()

    def get_db_name(self) -> str:
        return self.__db_name

class FilmsDBWorker(DBWorker):
    def __init__(self):
        super().__init__("films_db.sqlite")
        self.cur = self._connector.cursor()

    def get_info_from_db(self):
        res = self.cur.execute(
            """SELECT films.id, films.title,
            films.year, films.duration, genres.title
            FROM films
            JOIN genres ON films.genre = genres.id""")
        return res.fetchall()

    def get_genres(self):
        res = self.cur.execute(
            """SELECT * FROM genres"""
        )
        return res.fetchall()

    def add_film_in_db(self, film: Film):
        self.cur.execute(
            f"""INSERT INTO films (title, year, genre, duration)
            VALUES('{film.name}', {int(film.date)}, {int(film.genre)}, {film.time})
            """
        )
        self._connector.commit()

    def edit_film(self, new_film: Film, ID: int):
        self.cur.execute(
            f"""UPDATE films
            SET
            title = '{new_film.name}',
            year = {int(new_film.date)},
            genre = {int(new_film.genre)},
            duration = {new_film.time}
            WHERE
                id = {ID};
            """
        )
        self._connector.commit()

    def delete_from_db_by_id(self, ID: int):
        self.cur.execute(f"DELETE FROM films WHERE id = {ID}")
        self._connector.commit()
