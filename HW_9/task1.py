# 1. Напишите следующие функции:
#    * Нахождение корней квадратного уравнения
#    * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
#    * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
#    * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import json
import csv
import math
import os
import random


def gen_csv(count=3, start=1, stop=100, rows_min=100, rows_max=1000):
    with open("random_num.csv", "w", encoding="utf-8", newline="") as file_csv:
        writer = csv.writer(file_csv, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(
            [[random.randint(start, stop) for _ in range(count)] for _ in range(random.randint(rows_min, rows_max))]
        )


def read_csv(func):
    gen_csv()

    def wrapper():
        if os.path.exists("random_num.csv"):
            with open("random_num.csv", "r", encoding='utf-8', newline="") as file_csv:
                for item in csv.reader(file_csv, quoting=csv.QUOTE_NONNUMERIC):
                    func(*item)

                return func
        else:
            return func

    return wrapper


def save_json(func):
    def wrapper(*args, **kwargs):
        if os.path.exists(func.__name__ + ".json"):
            with open(func.__name__ + ".json", "r", encoding='utf-8') as file_json:
                res = json.load(file_json)
        else:
            res = []
        res.append({"args": [*args], "result": (func(*args, **kwargs))})
        with open(func.__name__ + ".json", "w", encoding='utf-8') as file_json:
            json.dump(res, file_json, indent=1)
        return func

    return wrapper


@read_csv
@save_json
def get_root(*args):
    a, b, c = args
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif d == 0:
        x1 = -b / (2 * a)
        return round(x1, 2)


get_root()
exit()
