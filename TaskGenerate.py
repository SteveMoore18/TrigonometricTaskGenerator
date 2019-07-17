#!usr/bin/env python3

'''
Этот модуль нужен для генерации выражений
Есть 3 уровня: простой, средний и сложный
Пример простого (generate_easy_task):
    sin(30°) + cos(45°)

Пример среднего:
    sin(-75°) * tg(π/2)

Пример сложного:
    (tg(946°) + sin(3π/2)) / 2 + cos(π/2)



'''



import math
import random

decimal_places = 10

# sin_a, cos_a, tg_a, ctg_a - если пользоватль выбрал с какими конкретно функциями хочет тренероваться
def generate_easy_task(sin_a, cos_a, tg_a, ctg_a):
    # Дефолтные градусы
    low_level_graduses = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
    graduses_size = len(low_level_graduses)

    operators = ['+', '-', '×', '÷']
    trig = []


    if sin_a == True:
        trig.append('sin({')
    if cos_a == True:
        trig.append('cos({')
    if tg_a == True:
        trig.append('tg({')
    if ctg_a == True:
        trig.append('ctg({')

    trig_size = len(trig)

    if trig_size == 0:
        return (0, 0)

    # Переменная, которую увидит пользователь
    temp_str_task = ''

    # Переменная, которую будет обрабатывать компьютер
    temp_str_task_c = ''

    # Генерируем количество операндов в выражении
    count_operands = random.randint(1, 3)

    # counter - нужен для обозначения аргументов в строке, для функции .format()
    counter = 0

    # Генерируем случайный пример
    for a in range(0, count_operands):
        # В temp_str_task сначала записываем тригонометрическую функцию, потом добавляем '}) ', а потом рандомный оператор
        temp_str_task += trig[random.randint(0, (trig_size - 1))] + str(counter) + '}°) ' + operators[random.randint(0, 3)] + ' '
        counter += 1

    # Удаляем 2 последних символа, т.к там может стоять оператор
    temp_str_task = temp_str_task[0:-2]
    temp_str_task_c = temp_str_task

    # Здесь будут храниться рандомно выбранные градусы из low_level_graduses, для того, чтобы их можно было записать в temp_str_task используя функцию .format()
    list_graduses = []
    for i in range(0, count_operands):
        # Заполняем случайными элементами из low_level_graduses
        list_graduses.append(low_level_graduses[random.randint(0, graduses_size - 1)])

    # Теперь  применяя функцию .format(), в аргумент передаем list_graduses и он заполняет строку градусами
    # И по сути, строчка пользователя готова
    temp_str_task = temp_str_task.format(*list_graduses)

    # Теперь займемся выражением для компьютера

    # Т.к котангенса нет в стандартной библиотеки math, то вы сделаем по формуле ctg = sin(a) / cos(a)
    # Для начала вычисляем на какой позиции находится котангенс
    ctg_pos = temp_str_task_c.find('ctg')

    # Эта переменная нужна для того, чтобы узнать в какой аргумент, функции format(), записывать значения
    arg_count = 0

    # Если ctg является вторым операндом, то arg_count будет 1
    if ctg_pos >= 9 and ctg_pos <= 18:
        arg_count = 1
    # И если ctg является третим операндом, то arg_count будет 2
    elif ctg_pos >= 20 and ctg_pos <= 29:
        arg_count = 2

    # Список для хранения радиан. То есть переводим список с градусами(list_graduses) в радианы, т.к синус, косинус и т.д принимают радианы
    list_radians = []
    for i in range(0, count_operands):
        # Берем элемент
        temp_grad = list_graduses[i]
        # И с помощью стандартной функции math.radians() библиотеки math, мы преобразуем градусы в радианы
        list_radians.append(round(math.radians(temp_grad), decimal_places))

    # И после всего этого, мы в переменную, с которой будет работать компьютер, записываем радианы, а также, если нашли котангес, то
    # идем по стандартной формуле sin(a) / cos(a)
    temp_str_task_c = temp_str_task_c.replace('ctg({' + str(arg_count) + '}°)',
                                              '(cos({' + str(arg_count) + '})/sin({' + str(arg_count) + '}))').format(
        *list_radians)

    temp_str_task_c = temp_str_task_c.replace('×', '*')
    temp_str_task_c = temp_str_task_c.replace('÷', '/')
    temp_str_task_c = temp_str_task_c.replace('°', '')
    temp_str_task_c = temp_str_task_c.replace(' ', '')
    temp_str_task_c = temp_str_task_c.replace('sin', 'math.sin')
    temp_str_task_c = temp_str_task_c.replace('cos', 'math.cos')
    temp_str_task_c = temp_str_task_c.replace('tg', 'math.tan')

    return (temp_str_task, temp_str_task_c)





