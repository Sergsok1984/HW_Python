# 1. Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
#
#    Задание №1:
#    Создайте класс Моя Строка, где будут доступны все возможности str,
#    дополнительно хранятся имя автора строки и время создания.
#
from time import time, strftime, gmtime


class MyStr(str):
    """Класс Моя Строка, где: доступны все возможности str,
    дополнительно хранятся имя автора строки и время создания"""

    def __new__(cls, value, name):
        """Расширяем метод new параметрами value & name"""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.creat_time = strftime('%H:%M:%S', gmtime(time()))
        return instance

    def __init__(self, value, name):
        """Инициализация для вывода информации для пользователя и программиста"""
        self.value = value
        self.name = name

    def __str__(self):
        """Вывод информации для пользователя"""
        return str({'value': self} | self.__dict__)

    def __repr__(self):
        """Вывод информации для программиста"""
        return f'MyStr("{self.value}", "{self.name}")'


# my_str = MyStr("5", 'John')
# print(my_str)
# print(repr(my_str))


# Задание №2:
# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При создании нового экземпляра класса старые данные из ранее созданных экземпляров сохраняются в пару списков-
# архивов, list-архивы также являются свойствами экземпляра.


class Archive:
    """Класс Архив, который хранит число и строку."""

    _instance = None

    def __new__(cls, *args):
        """Расширяем метод new"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive = []
        else:
            cls._instance.archive.append((cls._instance.num, cls._instance.value))
        return cls._instance

    def __init__(self, num, value):
        """Инициализация данных"""
        self.num = num
        self.value = value

    def __str__(self):
        """Вывод информации для пользователя"""
        return f'{self.num}, {self.value}, {self.archive}'

    def __repr__(self):
        """Вывод информации для программиста"""
        return f'Archive({self.num}, "{self.value}")'


# u_1 = Archive(1, "One")
# print(u_1)
# u_2 = Archive(2, "Two")
# print(f'{u_2.num = }, {u_2.value = }, {u_2.archive = }')
# print(repr(u_2))


# Задание №3:
# Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений. Добавьте сравнение прямоугольников по площади.
# Должны работать все шесть операций сравнения.

class Rectangle:
    """Класс Прямоугольник"""

    def __init__(self, length, width=None):
        """Инициализация данных"""
        self.length = length
        self.width = width if width else length

    def perimeter(self):
        """Расчет периметра"""
        return 2 * (self.length + self.width)

    def square(self) -> int:
        """Расчет площади"""
        return self.length * self.width

    def __add__(self, other):
        new_perimeter = self.perimeter() + other.perimeter()
        new_length = self.length + other.length
        new_width = new_perimeter / 2 - new_length
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_length = self.length - other.length
        new_width = new_perimeter / 2 - new_length
        return Rectangle(new_length, new_width)

    def __ge__(self, other):
        return self.square() >= other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __eq__(self, other):
        return self.square() == other.square()

    def __str__(self):
        """Вывод информации для пользователя"""
        return f'{self.length = }, {self.width = }, {self.perimeter() = }, {self.square() = }'

    def __repr__(self):
        """Вывод информации для программиста"""
        return f'Rectangle({self.length}, {self.width})'


# r1 = Rectangle(10, 7)
# r2 = Rectangle(5, 3)
# print(f'{r1.perimeter() = }, {r1.square() = }')
# print(f'{r2.perimeter() = }, {r2.square() = }')
# r3 = r1 - r2
# print(r3)
# print(repr(r3))
