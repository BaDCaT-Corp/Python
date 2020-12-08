'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def divide(_x, _y):
    return _x / _y

x = int(input('Введите числитель:'))
y = int(input('Введите знаменатель:'))
if y == 0:
    print('Делить на ноль нельзя')
else:
     print('Ответ:', divide(x,y))

'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод 
данных о пользователе одной строкой.
'''

def user_info_out(_name=None, _surname=None, _year=None, _city=None, _emal=None, _phone=None):
    print('Имя: ', _name, ' Фамилия: ', _surname, ' Год рождения: ', _year, ' Город проживания: ', _city, ' Email: ', _emal,
          ' Телефон: ', _phone)

dict_user = {'Имя': '', 'Фамилия': '', 'Год рождения': '', 'Город проживания': '', 'Email': '', 'Телефон': ''}
for f in dict_user.keys():
    dict_user[f] = input(f'{f}: ')

user_info_out(_name=dict_user['Имя'], _year=dict_user['Год рождения'], _phone=dict_user['Телефон'], _emal=dict_user['Email'],
              _city=dict_user['Город проживания'], _surname=dict_user['Фамилия'])


'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму 
наибольших двух аргументов.
'''

def max_value(_v1=int(), _v2=int(), _v3=int()):
    return int(_v1 + _v2 + _v3 - min(_v1, _v2, _v3))

v1 = int(input('Первое число:'))
v2 = int(input('Второе число:'))
v3 = int(input('Третье число:'))
print(max_value(v1, v2, v3))

'''
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''

def my_func_star(x, y):
    return x**y

def my_func(x, y):
    for i in range(y, 0, 1):
        x = x * x
    return 1/x

v1 = float(input('Действительное число:'))
v2 = int(input('Целое отрицательное число:'))
if v2 >= 0:
    print('Введено не отрицательное число')
else:
    print('Возведение в степень при помощи **', my_func_star(x=v1, y=v2))
    print('Возведение в степень при помощи цикла', my_func_star(x=v1, y=v2))

'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
 сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
  введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
   выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
    сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''
summ5 = 0

def calc_sum(_x):
    global summ5
    summ5 = summ5 + int(_x)
    return

l_exit = 0
row_number5 = []
while True:
    row_number5 = input('Выход - !, Введите строку чисел:').split()
    for i in range(len(row_number5)):
        if ord(row_number5[i]) == ord('!'):
            l_exit = 1
            break
        else:
            calc_sum(row_number5[i])
    if l_exit != 0:
        break

print(summ5)

'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
 первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
 из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
 буквы. Необходимо использовать написанную ранее функцию int_func().
'''

def int_func(_str=str):
    return _str.title()

list_str6 = []
list_str6 = input('Введите текст:').split()
for i in range(len(list_str6)):
    list_str6[i] = int_func(list_str6[i])

print(list_str6)


