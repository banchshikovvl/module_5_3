
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
#
# Необходимо дополнить класс House следующими специальными методами:
# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и
# возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:
#
# Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед
# выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House.

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        elif isinstance(other, int):
            self.number_of_floors += other
        return self

    def __radd__(self, other):
       return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        return self.__le__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def go_to(self, new_floor):
        list_ = []
        for i in range(1, self.number_of_floors + 1):
            list_.append(i)
        if new_floor in list_:
            for j in range(1, new_floor + 1):
                if j != new_floor:
                    print(j)
                else:
                    print(f'Приехали на {new_floor} этаж {self.name}')
                    print()
        else:
            print(f'В {self.name},такого этажа не существует')


dom1 = House('ЖК Эльбрус', 30)
dom2 = House('ЖК Уют', 10)

House.go_to(dom1, 16)
House.go_to(dom2, 9)

print()
print(f'{dom1.name}, количество этажей: {dom1.number_of_floors}')
print(f'{dom2.name}, количество этажей: {dom2.number_of_floors}')
print()
print('Магический метод __str__:')
print(dom1)
print(dom2)
print()
print('Магический метод __len__:')
print(len(dom1))
print(len(dom2))
print()
print('Метод "eq":', dom1 == dom2)
print()
print('Метод "add":', dom1 + 10)
print(dom1 == dom2)
print()
dom1 += 10
print('Метод "iadd":', dom1)
print()
print('Метод "radd":', 10 + dom2)
print()
print('Метод "gt":', dom1 > dom2)
print()
print('Метод "ge":', dom1 >= dom2)
print()
print('Метод "lt":', dom1 < dom2)
print()
print('Метод "le":', dom1 <= dom2)
print()
print('Метод "ne":', dom1 != dom2)

