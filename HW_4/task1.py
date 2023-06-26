# 1. Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
#    Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
#    (кроме переменной из одной буквы s) на None. Значения не удаляются,
#    а помещаются в одноимённые переменные без s на конце.

nums = 25
data = [36, 92]
strings = 'Hello world!'
s = 18
my_dict = globals()


def my_func(new_dict):
    for key in [key for key in new_dict if len(key) > 1 and key[-1] == 's']:
        new_dict[key[:-1]] = new_dict[key]
        new_dict[key] = None


print(nums)
print(data)
print(strings)
print(s)
print()

my_func(my_dict)

print(nums)
print(data)
print(strings)
print(s)
print()

print(num)
print(string)
print(s)
