# 3. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
#    Результаты обхода сохраните в файлы json, csv и pickle.
#    Для дочерних объектов указывайте родительскую директорию.
#    Для каждого объекта укажите файл это или директория.
#    Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов
#    и директорий.

import os
import json
import csv
import pickle


def get_dir_size(path):
    result = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                result += entry.stat().st_size
            elif entry.is_dir():
                result += get_dir_size(entry.path)
    return result


def get_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_dir_size(path)


def folder_walk(folder):
    result = []
    for dir_path, dir_names, file_names in os.walk(folder):
        for dir_n in dir_names:
            dir_size = get_size(dir_path + '\\' + dir_n)
            result.append({'obj': dir_n,
                           'parent': dir_path.split("\\")[-1],
                           'obj_type': 'directory',
                           'size': dir_size})
        for file in file_names:
            size = get_size(dir_path + '\\' + file)
            result.append({'obj': file,
                           'parent': dir_path.split("\\")[-1],
                           'obj_type': 'file',
                           'size': size})
    with open('result.json', 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, indent=2)
    with open('result.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['obj', 'parent', 'obj_type', 'size'])
        writer.writeheader()
        writer.writerows(result)
    with open('result.pickle', 'wb') as pickle_file:
        pickle.dump(result, pickle_file)
