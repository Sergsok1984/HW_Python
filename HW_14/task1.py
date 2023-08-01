# 1. Доработать класс Project

# 2. Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.


from Exceptions import LevelError, AccessError
import json


class Project:
    def __init__(self, users_lst=None):
        if users_lst is None:
            self.users_lst = []
        self.users_lst = users_lst
        self.admin = None

    @classmethod
    def get_users_list(cls):
        with open('users.json', 'r', encoding='utf-8') as f:
            my_dict = json.load(f)
            tmp = []
            for key in my_dict:
                for user in my_dict[key].items():
                    tmp.append(User(user[1], int(user[0]), int(key)))
            return cls(tmp)

    def login(self, name, u_id):
        user = User(name, u_id)
        for u in self.users_lst:
            if user == u:
                self.admin = u
                print(f'{u} - успешная авторизация')
                break
        else:
            raise AccessError(name, u_id)

    def add_user(self, name, u_id, level):
        if level < self.admin.level:
            raise LevelError(level)
        self.users_lst.append(User(name, u_id, level))

    def del_user(self, name, u_id, level):
        for i, user in enumerate(self.users_lst):
            if user == User(name, u_id, level):
                if user.level < self.admin.level:
                    raise LevelError(level)
                self.users_lst.pop(i)

    def save_to_json(self):
        with open('users.json', 'w', encoding='utf-8') as f:
            my_dict = {}
            for user in self.users_lst:
                key, value = user.level, ({user.u_id: user.name})
                temp_dict = {key: value}
                if key not in my_dict.keys():
                    my_dict.update(temp_dict)
                else:
                    my_dict[key].update(value)
            json.dump(my_dict, f, ensure_ascii=False)


class User:

    def __init__(self, name, u_id, level=None):
        self.name = name
        self.u_id = u_id
        self.level = level

    def __eq__(self, other):
        return self.name == other.name and self.u_id == other.u_id

    def __repr__(self):
        return f'{self.name=}, {self.u_id=}, {self.level=}'


# p = Project().get_users_list()
# print(p.users_lst)
# p.login('John', 1)
# print(p.admin)
# p.add_user("Sergei", 4, 2)
# print(p.users_lst)
# p.del_user("Bob", 3, 2)
# p.save_to_json()
