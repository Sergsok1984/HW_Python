# 2. Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали.
#    Превратите функции в методы класса. Задачи должны решаться через вызов методов экземпляра.

#    (task3 from HW_4)
#    Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
#    где ключ — значение переданного аргумента, а значение — имя аргумента.
#    Если ключ не хешируем, используйте его строковое представление.

from collections.abc import Hashable


class Dict:

    def __init__(self, my_dict=None):
        if my_dict is None:
            my_dict = {}
        self.my_dict = my_dict

    def get_dict(self, **kwargs):
        for key, value in kwargs.items():
            if not isinstance(value, Hashable):
                value = str(value)
            self.my_dict[value] = key
        return self.my_dict


print(f'{Dict().get_dict(num=1, name_list=["Sergey", "Andrey"], color_dict={1: "Red", 2: "Green", 3: "Yellow"})}')
