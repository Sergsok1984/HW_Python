# 1. Доработаем задачи 5-6. Создайте класс-фабрику.
#    Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
#    Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Fish(Animal):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def get_specific(self):
        return f'У {self.name} глубина обитания {self.depth} м.'


class Mammal(Animal):
    def __init__(self, name, wool_color):
        super().__init__(name)
        self.wool_color = wool_color

    def get_specific(self):
        return f'У {self.name} цвет шерсти {self.wool_color}.'


class Bird(Animal):
    def __init__(self, name, wings):
        super().__init__(name)
        self.wings = wings

    def get_specific(self):
        return f'У {self.name} размах крыльев {self.wings} м.'


class Fabric:

    @staticmethod
    def create_animal(animal_type, name, **kwargs):
        if animal_type == "mammal":
            return Mammal(name, **kwargs)
        elif animal_type == "bird":
            return Bird(name, **kwargs)
        elif animal_type == "fish":
            return Fish(name, **kwargs)
        else:
            raise ValueError("Invalid animal type")


mammal = Fabric().create_animal("mammal", "Timon", wool_color="коричневый")
print(f"{mammal.get_specific()}")
bird = Fabric().create_animal("bird", "Sapsan", wings=4)
print(f"{bird.get_specific()}")
fish = Fabric().create_animal("fish", "Nemo", depth=100)
print(f"{fish.get_specific()}")
