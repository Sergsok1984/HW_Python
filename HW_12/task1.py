# 1. Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра.
#   Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета
#   и по оценкам всех предметов вместе взятых.

import csv


class DescriptorName:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, str) or not value.isalpha() or not value.istitle():
            raise TypeError('Ф.И.О. должны начинаться с заглавной буквы и содержать только буквы')


class DescriptorLesson:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        with open('lessons.csv', 'r', encoding='utf-8') as f:
            read_csv = csv.reader(f)
            for line in read_csv:
                if value not in line:
                    raise ValueError(f'У студента нет предмета: {value}')


class Lesson:
    name_lesson = DescriptorLesson()

    def __init__(self, name_lesson):
        self.name_lesson = name_lesson
        self.list_grades = []
        self.list_test_scores = []

    def add_grade(self, grade):
        if grade < 2 or grade > 5:
            raise ValueError('Оценка должна быть в диапазоне от 2 до 5')
        self.list_grades.append(grade)

    def add_test_score(self, test_score):
        if test_score < 0 or test_score > 100:
            raise ValueError('Тестовый балл должен быть в диапазоне от 0 до 100')
        self.list_test_scores.append(test_score)

    def get_average_grade(self):
        return round(sum(self.list_grades) / len(self.list_grades))

    def get_average_test_score(self):
        return round(sum(self.list_test_scores) / len(self.list_test_scores))

    def __repr__(self):
        return self.name_lesson

    def __str__(self):
        return f'{self.name_lesson}\n\
                Средняя оценка по данному предмету: {self.get_average_grade()}\n\
                Средний балл по тестам по данному предмету: {self.get_average_test_score()}'


class Student:
    first_name = DescriptorName()
    patronymic = DescriptorName()
    last_name = DescriptorName()

    def __init__(self, first_name, patronymic, last_name):
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        self.list_lesson = []
        self.list_grades_aggregate = []

    def append_lesson(self, lesson: Lesson):
        self.list_lesson.append(lesson)

    def get_average_grade_aggregate(self):
        for lesson in self.list_lesson:
            self.list_grades_aggregate += lesson.list_grades
        print(f'Средняя оценка по всем предметам: '
              f'{round(sum(self.list_grades_aggregate) / len(self.list_grades_aggregate))}')

    def print_list_lesson(self):
        print(f'{self.first_name} {self.patronymic} {self.last_name}:')
        for lesson in self.list_lesson:
            print(lesson)
        self.get_average_grade_aggregate()

    def __str__(self):
        return f'{self.first_name} {self.patronymic} {self.last_name}: ' \
               f'{self.list_lesson}'


if __name__ == '__main__':
    stud_1 = Student('Cергей', 'Владимирович', 'Соколов')

    maths = Lesson('Математика')
    physics = Lesson('Физика')

    stud_1.append_lesson(maths)
    stud_1.append_lesson(physics)

    maths.add_grade(5)
    maths.add_grade(4)
    maths.add_grade(5)
    maths.add_test_score(84)
    maths.add_test_score(91)
    maths.add_test_score(95)

    physics.add_grade(4)
    physics.add_grade(5)
    physics.add_grade(4)
    physics.add_test_score(72)
    physics.add_test_score(57)
    physics.add_test_score(87)

    print(stud_1)
    stud_1.print_list_lesson()
