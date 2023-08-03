# 1. Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
#    Соберите информацию о содержимом в виде объектов namedtuple.
#    Каждый объект хранит:
#    * имя файла без расширения или название каталога,
#    * расширение, если это файл,
#    * флаг каталога,
#    * название родительского каталога.
#    В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
import logging
from collections import namedtuple
import os


def folder_walk(path):
    logging.basicConfig(filename='log.txt',
                        filemode='w',
                        format="{asctime} - {levelname}: {msg}",
                        style='{', level=logging.NOTSET,
                        encoding='utf-8')
    logger = logging.getLogger()
    FSObject = namedtuple('FSObject', 'name ext is_dir parent', defaults=['', '', False, ''])
    fs_objects = []
    for dir_path, dir_names, file_names in os.walk(path):
        parent = dir_path.split("\\")[-1]
        for dir_name in dir_names:
            obj_name, obj_ext = dir_name, None
            fs_objects.append(FSObject(name=obj_name, ext=obj_ext, parent=parent, is_dir=True))
            logger.info(msg=str(fs_objects[-1]))
        for file_name in file_names:
            obj_name, obj_ext = file_name.rsplit('.', 1)
            fs_objects.append(FSObject(name=obj_name, ext=obj_ext, parent=parent, is_dir=False))
            logger.info(msg=str(fs_objects[-1]))


parser = argparse.ArgumentParser()
parser.add_argument('-p', metavar='path')
args = parser.parse_args()

# folder_walk(r'D:\Serg\work')
