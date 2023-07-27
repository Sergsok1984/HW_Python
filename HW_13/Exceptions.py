class BasicExceptions(Exception):
    pass


class LevelError(BasicExceptions):
    def __init__(self, level):
        self.level = level

    def __str__(self):
        return "Внимание! Ошибка уровня доступа!"


class AccessError(BasicExceptions):
    def __init__(self, name, u_id):
        self.name = name
        self.u_id = u_id

    def __str__(self):
        return f"У пользователя {self.name= }, {self.u_id= } нет доступа!"
