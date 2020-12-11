'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:
    def __init__(self, _list):
        self.l_mx = _list

    def __str__(self):
        str=''
        for line in self.l_mx:
            str += f'{line}' + '\n'
        return str

list = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
my_matrix = Matrix(list)
print(my_matrix)
list = ((1, 2, 3, 3), (4, 5, 6, 6), (7, 8, 9, 9))
my_matrix2 = Matrix(list)
print(my_matrix2)

'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для
костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod

class AbsClothes(ABC):

    @abstractmethod
    def __init__(self, _name):
        self.name = _name

    @abstractmethod
    def fabric_consumption(self):
        return 0

class Cloths(AbsClothes):
    def __init__(self, _name):
        self.name = _name

    def fabric_consumption(self):
        pass

class Coat(Cloths):
    def __init__(self, _name, _size):
        super(Coat, self).__init__(_name)
        self.size = _size

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5

    def __str__(self):
        return f'Раcход ткани на {self.name} = {self.fabric_consumption}'

class Сostume(Cloths):
    def __init__(self, _name, _rise):
        super(Сostume, self).__init__(_name)
        self.rise = _rise

    @property
    def fabric_consumption(self):
        return self.rise * 2 + 0.3

    def __str__(self):
        return f'Раcход ткани на {self.name} = {self.fabric_consumption}'

coat = Coat('Coat autumn', 52)
costume = Сostume('Costume festive', 1.84)
coat2 = Coat('Coat winter', 54)

print(coat)
print(costume)

print('Общий расход', coat.fabric_consumption + costume.fabric_consumption + coat2.fabric_consumption)

'''
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы
методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
'''

class Cell:
    def __init__(self, _count):
        self.count = _count

    def __setattr__(self, attr, value):
        if attr == "count":
            self.__dict__[attr] = int(value)

    def __add__(self, other):
        cell = Cell(self.count + other.count)
        return cell

    def __sub__(self, other):
        cell = Cell(0)
        if self.count >= other.count:
             cell.count = self.count - other.count
        else:
            print('Невозможно выполнить вычитание ', self.count, '-', other.count)
        return cell

    def __mul__(self, other):
        cell = Cell(self.count * other.count)
        return cell

    def __truediv__(self, other):
        cell = Cell(0)
        if other.count == 0:
            print('Деление на 0!')
        else:
            cell.count = self.count / other.count
        return cell

    def __str__(self):
        return f'Количество клеток: {self.count}'

    def make_order(self, _line_count):
        str = ''
        for i in range(1, self.count+1):
            str += '*'
            if i % _line_count == 0:
                str += '\n'
        return str


cell_1 = Cell(5.1)
cell_2 = Cell(2)
cell_3 = Cell(3)

print('Исходные клетки:')
print(cell_1)
print(cell_2)
print(cell_3)
print('\n')

cell_o1 = cell_1 + cell_2
cell_o2 = cell_2 - cell_1
cell_o6 = cell_1 / cell_o2
cell_o3 = cell_2 * cell_1
cell_o4 = cell_2 / cell_1
cell_o5 = cell_1 / cell_2

print('\n', 'Клетки результата:')
print(cell_o1)
print(cell_o2)
print(cell_o3)
print(cell_o4)
print(cell_o5)
print(cell_o6)

print('\n', 'Клетки в ряд:')
print(cell_o1.make_order(3))
print('\n')
print(cell_o1.make_order(5))