'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

open_file_1 = open("Lesson5_1.txt", "w")

while True:
    row_1 = input('Введите новую строку:')
    if not row_1:
        break
    else:
        open_file_1.writelines(row_1)
        open_file_1.write('\n')

open_file_1.close()

'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

lines = 0

with open('Lesson5_2.txt') as file2:
    for line in file2:
        lines = lines + 1
        print('Всего символов в строке', lines, ':', len(line))

print('Всего строк:', lines)

'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''
count = 0
sum = 0
value = ''
line = []

with open('Lesson5_3.txt') as file3:
    for line in file3:
        count = count + 1
        value = line.split(' ')
        if int(value[1]) < 20000:
            print('Имеет оклад менее 20 тыс.', value[0])
        sum = sum + int(value[1])
sum = sum/count

print('Средний оклад:', '%f' % sum)

'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

l_dict4 = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'}

with open('Lesson5_4_in.txt', 'r', encoding='utf-8') as file4_in:
    lines = file4_in.readlines()

with open('Lesson5_4_out.txt', 'w', encoding='utf-8') as file4_out:
    for line in lines:
        for items in l_dict4.items():
            line = line.replace(items[0], items[1])
        file4_out.write(line)

'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
l_sum = 0
with open('Lesson5_5.txt', 'w') as file5:
    nums = input('Ведите набор чисел:')
    file5.write(nums + '\n')
    nums = nums.split()
    for num in nums:
        l_sum += int(num)
    file5.write(str(l_sum))

print('Сумма чисел:', l_sum)

'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
import re

dict_out = {}

with open('Lesson5_6.txt', 'r', encoding='utf-8') as file6:
    lines = file6.readlines()

for line in lines:
    value = line.split(' ')
    sum = 0
    for v in value:
        v = re.sub('\D', '', v)
        try:
            sum += int(v)
        except Exception:
            pass
    dict_out.update({value[0]: sum})

print(dict_out)

'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
    форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
import json

average_income = []
dict7 = {}
company_info = []

with open('Lesson5_7.txt', encoding='utf-8') as file7:
    lines = file7.readlines()

for line in lines:
    company_info = line.split()
    income = int(company_info[2]) - int(company_info[3])
    dict7[company_info[0]] = income
    if income > 0:
        average_income.append(income)
average_profit = sum(average_income) / len(average_income)

out_data = [dict7, {'average_profit': average_profit}]

with open('Lesson5_7.json', 'w') as file7_json:
    json.dump(out_data, file7_json)