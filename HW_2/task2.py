# 2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
#    Программа должна возвращать сумму и произведение* дробей.
#    Для проверки своего кода используйте модуль fractions.

import fractions

numerator_1, denominator_1 = map(int, input('Введите числитель и знаменатель первой дроби, пример a/b: ').split("/"))
numerator_2, denominator_2 = map(int, input('Введите числитель и знаменатель второй дроби, пример a/b: ').split("/"))

d1 = numerator_1 * numerator_2
g1 = numerator_1 * denominator_2 + numerator_2 * denominator_1
d2 = g2 = denominator_1 * denominator_2


def get_gcd(a, b):
    gcd = None
    if a > b:
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd


gcd_sum = get_gcd(g1, g2)
gcd_mult = get_gcd(d1, d2)

print(f'Сумма дробей: {int(g1 / gcd_sum)}/{int(g2 / gcd_sum)}')
print(f'Произведение дробей: {int(d1 / gcd_mult)}/{int(d2 / gcd_mult)}')

f1 = fractions.Fraction(numerator_1, denominator_1)
f2 = fractions.Fraction(numerator_2, denominator_2)

print(f"Проверка суммы дробей: {f1 + f2}")
print(f"Проверка произведения дробей: {f1 * f2}")
