from pathlib import Path

from task1 import pickle_to_csv
from task2 import csv_to_pickle_string
from task3 import folder_walk

if __name__ == '__main__':
    pickle_to_csv('users.pickle')
    csv_to_pickle_string(Path('users.csv'))
    folder_walk(r'C:\Users\Sergey')
