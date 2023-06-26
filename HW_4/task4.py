# 4. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
#    Дополнительно сохраняйте все операции поступления и снятия средств в список.

#    Напишите программу банкомат.
#    ✔ Начальная сумма равна нулю
#    ✔ Допустимые действия: пополнить, снять, выйти
#    ✔ Сумма пополнения и снятия кратны 50 у.е.
#    ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
#    ✔ После каждой третьей операции пополнения или снятия начисляются проценты - 3%
#    ✔ Нельзя снять больше, чем на счёте
#    ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
#    ✔ Любое действие выводит сумму денег

import sys

BALANCE = 0
MIN = 50
MAX = 5_000_000
RATE = 0.015
BONUS_RATE = 0.03
COUNT = 0
TAX = 0.1
op_list = []


def add_money():
    global COUNT, BALANCE
    money = int(input('Введите сумму пополнения, кратную 50 у.е.: '))
    if money % 50 == 0:
        BALANCE += money
        op_list.append(f"Пополнение: {money}")
        print(f'Вы пополнили счет на сумму: {money} у.е. ')
        COUNT += 1.
    else:
        print('Сумма пополнения не кратна 50 у.е.')


def add_bonus():
    global BONUS_RATE, BALANCE
    bonus_sum = BALANCE * BONUS_RATE
    BALANCE += BALANCE * BONUS_RATE
    op_list.append(f"Начислен бонус: {bonus_sum}")
    print(f'Вам начислен бонус: {bonus_sum} у.е.')


def get_money():
    global COUNT, BALANCE, RATE
    money = int(input('Введите сумму снятия, кратную 50 у.е.: '))
    if money > BALANCE:
        print('Запрашиваемая сумма больше, чем сумма на счете')
    elif money % 50 == 0:
        if money * RATE < 30:
            rate = 30
        elif money * RATE > 600:
            rate = 600
        else:
            rate = money * RATE
        BALANCE = BALANCE - money - rate
        op_list.append(f"Снятие: {money}")
        op_list.append(f"Комиссия за cнятие: {rate}")
        print(f'Вы сняли со счета: {money} у.е., комиссия за снятие: {rate} у.е.')
        COUNT += 1
    else:
        print('Сумма снятия не кратна 50 у.е.')


def start():
    global BALANCE
    while True:
        print(f'Cумма на счету составляет: {BALANCE} у.е.')
        print("Выберите операцию:\n\
    1 - пополнить\n\
    2 - снять\n\
    3 - список операций\n\
    4 - выйти")
        choice = input("Введите номер операции: ")
        if BALANCE > MAX:
            taxe = BALANCE * TAX
            BALANCE -= taxe
            op_list.append(f"Списание налога на богатсво: {taxe}")
            print(f'С вас списали налог на богатство в размере: {taxe} у.е.')

        match choice:
            case '1':
                add_money()

            case '2':
                get_money()

            case '3':
                print(op_list)

            case '4':
                sys.exit()

        if COUNT % 3 == 0:
            add_bonus()
        else:
            pass


start()
