from src.item import Item


class MixinLog:

    def __init__(self):
        self._language = "EN"

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"


class Keyboard(Item, MixinLog):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
