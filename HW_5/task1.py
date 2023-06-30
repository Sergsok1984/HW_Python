# 1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
#    Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла

import os

full_path = 'C:/Users/sergs/Documents/GB/HW_Python/HW_5/task1.py'


def get_tuple(file_path):
    path, file_name = os.path.split(file_path)
    name, extension = os.path.splitext(file_name)
    return path, name, extension


print(get_tuple(full_path))
