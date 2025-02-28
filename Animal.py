from encodings import normalize_encoding
from random import random


class Animal:
    especie=None
    id=None
    born_year=None

    def __init__(self, name,born_year,especie):
        self.name = name
        self.born_year=born_year
        self.especie=especie
        id=random.randint(0,1000)
    @classmethod
    def firstmethod(cls):
        return id

    @staticmethod
    def getid():
        return id

