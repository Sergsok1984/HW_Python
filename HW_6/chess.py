# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки
# ферзей в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок

from random import randint

__all__ = ['check_queen']

queen_point = ['22', '85', '36', '64', '43', '78', '17', '51']
N = 8


def check_queen(list_point):
    x = []
    y = []
    flag = True
    for i in range(N):
        x.append(int(list_point[i][0]))
        y.append(int(list_point[i][1]))

    for i in range(N):
        for j in range(i + 1, N):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                flag = False
    return flag


def get_random_point():
    list_ = []
    list_x = []
    list_y = []
    while len(list_) < N:
        num = randint(11, 88)

        if str(num) not in list_ and num % 10 != 0 and num % 10 != 9 and num // 10 not in list_x \
                and num % 10 not in list_y:
            list_x.append(num // 10)
            list_y.append(num % 10)
            list_.append(str(num))
    return list_


if __name__ == "__main__":
    print(get_random_point())
    print(check_queen(get_random_point()))

    count = 0
    while count < 4:
        b = get_random_point()
        a = check_queen(b)
        if a:
            count += 1
            print(count)
            print(b)
