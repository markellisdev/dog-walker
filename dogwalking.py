import sqlite3

class User():

    def __init__(self, first_name, last_name, email, username):
        self.__first_name = first_name # __ double underscores preface is private-ish
        self.__last_name = last_name
        self.__email = email
        self.__username = username

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__first_name

    def get_email(self):
        return self.__email

    def get_username(self):
        return self.__username

    def get_dogs(self):
