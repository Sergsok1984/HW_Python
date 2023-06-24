# 1. Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга,
#    а значение — кортеж вещей. Ответьте на вопросы:
#    * Какие вещи взяли все три друга?
#    * Какие вещи уникальны, есть только у одного друга?
#    * Какие вещи есть у всех друзей кроме одного
#      и имя того, у кого данная вещь отсутствует?
#    * Для решения используйте операции с множествами. Код должен расширяться
#      на любое большее количество друзей.

dict_things = {
    "Вася": ("Палатка", "Спички", "Веревка", "Книга"),
    "Андрей": ("Палатка", "Спички", "Гитара", "Удочка", "Деньги"),
    "Петр": ("Палатка", "Спички", "Веревка", "Термос")
}


def things_all_friends(things):
    list_all = []
    for v in things.values():
        list_all += v
    list_all_things = set(list_all)
    print(f"Список вещей, которые взяли все три друга: {list_all_things}")


def unique_dict(things):
    unique_things_dict = {}
    no_things_dict = {}
    for i in things:
        unique_things = set(things[i])
        no_things = set()
        for j in things:
            if j != i:
                unique_things -= set(things[j])
                if not no_things:
                    no_things |= (set(things[j]))
                else:
                    no_things.intersection_update(set(things[j]))
        unique_things_dict[i] = unique_things
        no_things_dict[i] = no_things - set(things[i])
    print(f"Уникальные вещи у каждого друга: {unique_things_dict}\n"
          f"Вещи, которые есть у всех друзей кроме одного: {no_things_dict}")


things_all_friends(dict_things)
unique_dict(dict_things)
