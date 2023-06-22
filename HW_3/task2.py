# 2. Дан список повторяющихся элементов.
#    Вернуть список с дублирующимися элементами.
#    В результирующем списке не должно быть дубликатов.

my_list = [3, 15, 22, 3, 3, 6, 8, 15, 9, 22]
res_list = []

for i in my_list:
    if my_list.count(i) > 1:
        if i not in res_list:
            res_list.append(i)
print(res_list)
