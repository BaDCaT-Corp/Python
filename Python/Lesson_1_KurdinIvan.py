print('1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько'
      ' чисел и строк и сохраните в переменные, выведите на экран.')

print('Введите первое число')
in_number_1 = input()
print('Введите второе число')
in_number_2 = input()

multiplier = 5

print('Concatenation:', in_number_1 + in_number_2)

in_number_1 = int(in_number_1)
in_number_2 = int(in_number_2)

print('Sum:', in_number_1 + in_number_2)
print('Odds:', in_number_1 - in_number_2)
print('Multiplication:', in_number_1 * in_number_2)
print('Division:', in_number_1 / in_number_2)

print('2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс'
      ' Используйте форматирование строк.')
print('Введите количество секунд')
in_count_sec = input()
in_count_sec = int(in_count_sec)
hour = in_count_sec // 3600
minutes = ( in_count_sec - hour * 3600 ) // 60
sec = in_count_sec % 60

print('Результат в формате hh:mm:ss', f'{hour:02}:{minutes:02}:{sec:02}')

print('3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.'
      'Считаем 3 + 33 + 333 = 369.' )
print('Введите число n:')
in_num_1 = input()
in_num_2 = in_num_1 + in_num_1
in_num_3 = in_num_1 + in_num_1 + in_num_1
sum = int(in_num_1) + int(in_num_2) + int(in_num_3)
print('Результат в формате n + nn + nnn:', in_num_1, '+', in_num_2, '+', in_num_3, '=', sum)

print('4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте'
      'цикл while и арифметические операции.' )
print('Введите целое положительное число:')
in_text = input()
remainder = int(in_text)
number = max_number = 0

while (remainder > 0):
    number = remainder % 10
    remainder = remainder // 10
    if number > max_number:
        max_number = number

print('Максимальное число:', max_number)

print('5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом'
      'работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите'
      'соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки'
      '(соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в'
      'расчете на одного сотрудника.')

print('Введите выручку:')
in_proceeds = int(input())
print('Введите издержки:')
in_cost = int(input())

if in_proceeds > in_cost:
    print('Прибыль')
    profit = in_proceeds - in_cost
    rentability = profit / in_proceeds
    print('Рентабельность:', '%.2f' % rentability)
    print('Введите количество сотрудников фирмы:')
    count_worker = int(input())
    profit_on_worker = profit / count_worker
    print('Прибыль на сотрудника:', '%.2f' % profit_on_worker)
else:
    print('Убыток');

print('6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день '
      'спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который '
      'общий результат спортсмена составить не менее b километров. Программа должна принимать значения '
      'параметров a и b и выводить одно натуральное число — номер дня.')

# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

print('Введите А:')
in_a = int(input())
print('Введите B:')
in_b = int(input())
count = 1
a = in_a
b = in_b

while (a < b):
    a = a * 1.1
    count = count + 1

print(count)
# print('Ответ: на ', count, '-й день спортсмен достиг результата — не менее', in_b, 'км.')



