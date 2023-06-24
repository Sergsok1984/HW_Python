# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
#    Не учитывать знаки препинания и регистр символов.
#    За основу возьмите любую статью из википедии или из документации к языку.

import re

text = 'Последовательность инструкций, предназначенная для многократного исполнения, называется телом цикла.\
        Единичное выполнение тела цикла называется итерацией. Выражение, определяющее, будет в очередной раз \
        выполняться итерация или цикл завершится, называется условием выхода или условием окончания цикла \
        (либо условием продолжения в зависимости от того, как интерпретируется его истинность — как признак \
        необходимости завершения или продолжения цикла). Переменная, хранящая текущий номер итерации, \
        называется счётчиком итераций цикла или просто счётчиком цикла. Цикл не обязательно содержит счётчик, \
        счётчик не обязан быть один — условие выхода из цикла может зависеть от нескольких изменяемых \
        в цикле переменных, а может определяться внешними условиями (например, наступлением \
        определённого времени), в последнем случае счётчик может вообще не понадобиться.'

text = re.sub(r'\W', ' ', text).split()

dict_text = {}
for word in text:
    dict_text.setdefault(word, text.count(word))

res_list = list(dict_text.items())

res_list.sort(key=lambda i: i[1], reverse=True)

for e in enumerate(res_list[:10], 1):
    print(f"{e}")
