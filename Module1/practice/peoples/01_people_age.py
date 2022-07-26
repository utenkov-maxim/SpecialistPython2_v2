class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age

    def change_age(self, new_age):
        # Корректным возрастом считаем целое число от 1 до 100
        # Если задан некорректный возраст, выводим "некорректное значение для возраста" и оставляем старое значение
        # Метод ничего не возвращает в качестве результата, а только меняем свойство self.age на значение new_age
        if type(new_age) == int and 1 <= new_age <= 100:
            self.__age = new_age
        else:
            raise ValueError("Некорректное значение для возраста")

    def full_name(self):
        return f"{self.surname} {self.name}"

    def full_info(self):
        return f"Человек: {self.surname} {self.name} и ему {self.__age} лет"


# Создадим двух человек:
people1 = People("Иван", "Уткин", 27)
people2 = People("Алексей", "Перов", 35)
people3 = People("Василий", "Быстров", 65)

print(people1.full_info())
print(people2.full_info())
print(people3.full_info())

print("Меняем возраст людей")
try:
    people1.change_age(45)
except ValueError as ex:
    print(ex)
try:
    people2.change_age("help")
except ValueError as ex:
    print(ex)
try:
    people3.change_age(25)
except ValueError as ex:
    print(ex)
print(people1.full_info())
print(people2.full_info())
print(people3.full_info())