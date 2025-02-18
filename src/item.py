import csv
import os.path

from src.InstantiateCSVError import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, path_file):
        """
        Get csv file and create 5 classes
        """
        cls.all.clear()

        if not os.path.exists(path_file):
            raise FileNotFoundError('Отсутствует файл item.csv')

        else:
            with open(path_file, 'r', encoding='windows-1251') as csv_file:
                file = csv.DictReader(csv_file)

                for row in file:
                    if len(row) != 3:
                        raise InstantiateCSVError
                    cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(string):
        """
        Change from int-str to int
        """
        clean_string = string.strip().replace(',', '.')
        return int(float(clean_string))
