# 1. Выведите в консоль таблицу умножения от 2х2 до 9х10, как на школьной тетрадке.

START = 2
STOP = 10

for i in range(START, STOP):
    for j in range(START, STOP // 2 + 1):
        print(f"{j} X {i} = {i * j:>2}", end="     ")
    print()
print()
for i in range(START, STOP):
    for j in range(STOP // 2 + 1, STOP):
        print(f"{j} X {i} = {i * j:>2}", end="     ")
    print()
