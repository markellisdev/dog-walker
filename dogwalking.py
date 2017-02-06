import sqlite3

class User():

    def __init__(self, first_name, last_name, email, username):
        self.__first_name = first_name # __ double underscores preface is private-ish
        self.__last_name = last_name
        self.__email = email
        self.__username = username

    def get_dogs(self):
