# 3. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
#    где ключ — значение переданного аргумента, а значение — имя аргумента.
#    Если ключ не хешируем, используйте его строковое представление.

from collections.abc import Hashable


def get_dict(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        if not isinstance(value, Hashable):
            value = str(value)
        my_dict[value] = key
    print(my_dict)


get_dict(num=1, name_list=["Sergey", "Andrey"],
         color_dict={1: "Red", 2: "Green", 3: "Yellow"})
