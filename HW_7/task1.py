# 1. Напишите функцию группового переименования файлов.
#    Она должна:
#    * принимать в качестве аргумента желаемое конечное имя файлов.
#      При переименовании в конце имени добавляется порядковый номер.
#    * принимать в качестве аргумента расширение исходного файла.
#      Переименование должно работать только для этих файлов внутри каталога.
#    * принимать в качестве аргумента расширение конечного файла.
#    Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>


import os
from pathlib import Path


def get_rename_filename(new_name: str, old_extention: str, new_extention: str):
    position = 0
    for file in os.listdir():
        if file.endswith(old_extention):
            position += 1
            Path(file).rename(f"{file.split('.')[0]}_{new_name}_{position}.{new_extention}")


if __name__ == "__main__":
    get_rename_filename('test', 'txt', 'md')
