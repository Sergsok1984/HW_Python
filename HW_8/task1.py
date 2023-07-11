# 1. Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
#    Для тестированию возьмите pickle версию файла из предыдущей задачи.
#    Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv


def pickle_to_csv(pickle_file):
    with (open(pickle_file, 'rb') as f1,
          open("users.csv", "w", newline='', encoding='utf-8', ) as f2,
          ):
        p_file = pickle.load(f1)
        field = []
        rows = []
        for item in p_file:
            rows.append(item)
            for key in item:
                if key not in field:
                    field.append(key)
        level, u_id, name, hash_name = field
        csv_write = csv.DictWriter(f2, fieldnames=[level, u_id, name, hash_name])
        csv_write.writeheader()
        csv_write.writerows(rows)
