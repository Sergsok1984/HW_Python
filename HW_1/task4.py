# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
count = 10
res = ""

num = randint(LOWER_LIMIT, UPPER_LIMIT)
while count > 0:
    n = int(input('Введите число от 0 до 1000: '))
    count -= 1
    if n > num:
        res = f'Меньше, осталось попыток: {count}'
    elif n < num:
        res = f'Больше, осталось попыток: {count}'
    else:
        res = f'Победа, в угадали с {count} попытки!'
        break
    print(res)
res = 'Попытки закончились, вы проиграли'
print(res)
