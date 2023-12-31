# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN = 2
MAX = 100_000
count = 0
res = ''

num = int(input(f'Введите число от {MIN} до {MAX}: '))
if MIN <= num <= MAX:
    for i in range(MIN, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 1
    if count <= 0:
        res = 'Число простое'
    else:
        res = 'Число составное'
else:
    res = 'Недопустимое число'
print(res)
