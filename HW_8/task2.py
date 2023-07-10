# 2. Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
#    Распечатайте его как pickle строку.

import pickle
from pathlib import Path


def csv_to_pickle_string(file: Path):
    with open(file, 'r', encoding='utf-8') as f_csv:
        print(pickle.dumps(f_csv.read()))


if __name__ == '__main__':
    csv_to_pickle_string(Path('users.csv'))
