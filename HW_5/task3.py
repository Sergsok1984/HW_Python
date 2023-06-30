# 3. Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def get_fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for i in get_fib(10):
    print(i)
