import sqlite3

class Registrar():

    def register_user(self, user):
        with sqlite3.connect("dogwalking.db") as doge:
            cursor = doge.cursor() #cursor is doing the work

            try:
                cursor.execute("SELECT * FROM User")
                users = cursor.fetch_all()
            except OpertionalError:
                cursor.execute("""
                CREATE TABLE User
                    (
                        user_id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        username TEXT NOT NULL
                    )
                """)

            cursor.execute("""
            INSERT INTO User VALUES ({}, '{}', '{}', '{}', '{}')
            """.format(None,
                        user.get_first_name(),
                        user.get_last_name(),
                        user.get_email(),
                        user.get_username())
            )

    def user_is_registered(self, user):
        with sqlite3.connect("dogwalking.db") as doge:
            cursor = doge.cursor() #cursor is doing the work

            try:

                cursor.execute("""
                    SELECT * FROM User
                    WHERE first_name='{}'
                    AND last_name='{}'
                    AND email='{}'
                    AND username='{}'
                """.format(user.get_first_name(),
                            user.get_last_name(),
                            user.get_email(),
                            user.get_username()))
            

    def register_dog(self, user, dog):
        pass