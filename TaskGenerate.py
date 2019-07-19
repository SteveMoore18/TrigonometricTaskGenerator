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

operators = ['+', '-', '×', '÷']

# sin_a, cos_a, tg_a, ctg_a - если пользоватль выбрал с какими конкретно функциями хочет тренероваться
def generate_easy_task(sin_a, cos_a, tg_a, ctg_a):
    # Дефолтные градусы
    low_level_graduses = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
    graduses_size = len(low_level_graduses)


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



def generate_middle_task(sin_a, cos_a, tg_a, ctg_a):
    radians = {
        'π/6' : round(math.pi / 6, decimal_places),
        'π/4' : round(math.pi / 4, decimal_places),
        'π/3' : round(math.pi / 3, decimal_places),
        'π/2' : round(math.pi / 2, decimal_places),
        '2π/3': round(2 * math.pi / 3, decimal_places),
        '3π/4': round(3 * math.pi / 4, decimal_places),
        '5π/6': round(5 * math.pi / 6, decimal_places),
        'π'   : round(math.pi, decimal_places),
        '3π/2': round(3 * math.pi / 2, decimal_places),
        '2π'  : round(2 * math.pi, decimal_places),
    }

    middle_level_graduses = [30, 45, 60, 75, 90, 105, 120, 135, 150, 280, 180, 330, 270, 360]
    m_l_g_size = len(middle_level_graduses)

    middle_level_radians   = ['π/4', 'π/4', 'π/3', 'π/2', '2 × π/3', '3 × π/4', '5 × π/6', 'π', '3 × π/2', '2 × π']
    m_l_r_size = len(middle_level_radians)

    trig = []

    temp_str_task = ''

    if sin_a == True:
        trig.append('sin({')
    if cos_a == True:
        trig.append('cos({')
    if tg_a == True:
        trig.append('tg({')
    if ctg_a == True:
        trig.append('ctg({')

    trig_size = len(trig)


    count_operands = random.randint(1, 3)

    # counter - нужен для обозначения аргументов в строке, для функции .format()
    counter = 0

    # Генерируем случайный пример
    for a in range(0, count_operands):
        # В temp_str_task сначала записываем тригонометрическую функцию, потом добавляем '}) ', а потом рандомный оператор
        temp_str_task += trig[random.randint(0, (trig_size - 1))] + str(counter) + '}) ' + operators[
            random.randint(0, 3)] + ' '
        counter += 1

    temp_str_task = temp_str_task[0:-2]
    temp_str_task_c = temp_str_task

    list_arguments = []
    for arg in range(0, count_operands):
        g_or_r = random.randint(1, 2)

        if g_or_r == 1:
            num = middle_level_graduses[random.randint(0, m_l_g_size - 1)]
            list_arguments.append(str(num) + '°') # Здесь мы добавляем '°' только на число, а не на радианы
        elif g_or_r == 2:
            num = middle_level_radians[random.randint(0, m_l_r_size - 1)]
            list_arguments.append(num)

    temp_str_task = temp_str_task.format(*list_arguments)

    ctg_pos = temp_str_task_c.find('ctg')

    arg_count = 0

    # Если ctg является вторым операндом, то arg_count будет 1
    if ctg_pos >= 9 and ctg_pos <= 18:
        arg_count = 1
    # И если ctg является третим операндом, то arg_count будет 2
    elif ctg_pos >= 20 and ctg_pos <= 29:
        arg_count = 2


    list_radians = []
    for i in range(0, count_operands):
        temp_arg = list_arguments[i]
        temp_arg = temp_arg.replace('π', 'math.pi')
        temp_arg = temp_arg.replace('°', '')
        temp_arg = temp_arg.replace('×', '*')

        if temp_arg.find('pi') != -1:
            list_radians.append(round(eval(temp_arg), decimal_places))
        else:
            list_radians.append(round(math.radians(float(temp_arg)), decimal_places))



    # идем по стандартной формуле sin(a) / cos(a)
    temp_str_task_c = temp_str_task_c.replace('ctg({' + str(arg_count) + '})',
                                              '(cos({' + str(arg_count) + '})/sin({' + str(arg_count) + '}))').format(*list_radians)

    temp_str_task_c = temp_str_task_c.replace('×', '*')
    temp_str_task_c = temp_str_task_c.replace('÷', '/')
    temp_str_task_c = temp_str_task_c.replace('°', '')
    temp_str_task_c = temp_str_task_c.replace(' ', '')
    temp_str_task_c = temp_str_task_c.replace('sin', 'math.sin')
    temp_str_task_c = temp_str_task_c.replace('cos', 'math.cos')
    temp_str_task_c = temp_str_task_c.replace('tg', 'math.tan')


    return (temp_str_task, temp_str_task_c)

