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


Самая главная функция - строка 140


'''



import math
import random

decimal_places = 10

class Generate:

    sin_a = cos_a = tg_a = ctg_a = False

    graduses_list       = []
    graduses_list_size  = 0

    trigonomentric_funcs      = []
    trigonomentric_funcs_size = 0

    radian_lists = ['π/4', 'π/4', 'π/3', 'π/2', '2 × π/3', '3 × π/4', '5 × π/6', 'π', '3 × π/2', '2 × π']
    radian_lists_size = len(radian_lists)

    operators = []

    task_for_user = ''
    task_for_comp = ''

    count_operands = 0

    def __init__(self, sin_a, cos_a, tg_a, ctg_a):
        self.sin_a = sin_a
        self.cos_a = cos_a
        self.tg_a  = tg_a
        self.ctg_a = ctg_a

        self.operators = ['+', '-', '×', '÷']

    # Здесь мы инициализируем, какие пункты выбраны (синус, косинус и т.д)
    def __init_trigonometric_list(self):
        if self.sin_a == True:
            self.trigonomentric_funcs.append('sin({')
        if self.cos_a == True:
            self.trigonomentric_funcs.append('cos({')
        if self.tg_a == True:
            self.trigonomentric_funcs.append('tg({')
        if self.ctg_a == True:
            self.trigonomentric_funcs.append('ctg({')

        self.trigonomentric_funcs_size = len(self.trigonomentric_funcs)

    # Здесь генерируем шаблон для выражения.
    # К примеру: sin({0}) + cos({1}) * tg({2})
    def __generate_template_task(self):
        # Нужен для обозначений аргументов в {}.
        # Это нужно, чтобы из списка, к примеру градусов, мы могли сразу
        # добавлять их в шаблон используя .format()
        counter_args = 0

        # Генерируем случайный пример
        for a in range(0, self.count_operands):
            # Случайно выбираем тригонометрическую функцию
            trig_func = self.trigonomentric_funcs[random.randint(0, (self.trigonomentric_funcs_size - 1))]

            # Случайно выбираем оперератор (+, -, *, /)
            operator  = self.operators[random.randint(0, 3)]

            self.task_for_user += trig_func + str(a) + '}) ' + operator + ' '
            counter_args += 1

    # Здесь мы заменяем котангенс на формулу cos(a) / sin(a)
    # Т.к в стандартной библиотеки math, нет котангенса
    def __replace_ctg(self):

        # Делаем это столько, сколько операндов
        for i in range(0, self.count_operands):
            # Вычисляем позицию котангенса
            ctg_pos = self.task_for_comp.find('ctg')

            # Если не нашли, то выходим
            if ctg_pos == -1:
                return 0

            # Узнаем какой аргумент стоит в {}
            # +5 т.к нужно пройти 5 позиций,прежде чем доберемся до аргумента
            arg_count = int(self.task_for_comp[ctg_pos + 5])

            temp_ctg = 'ctg({' + str(arg_count) + '})'

            # Простая формула cos(a) / sin(a)
            temp_replaced_ctg = '(cos({' + str(arg_count) + '})/sin({' + str(arg_count) + '}))'

            # Замена
            self.task_for_comp = self.task_for_comp.replace(temp_ctg, temp_replaced_ctg)

    # Здесь заменяем спец. символы на обычные, которые понимает python
    def __change_task_comp(self):
        self.task_for_comp = self.task_for_comp.replace('×', '*')
        self.task_for_comp = self.task_for_comp.replace('÷', '/')
        self.task_for_comp = self.task_for_comp.replace('°', '')
        self.task_for_comp = self.task_for_comp.replace(' ', '')
        self.task_for_comp = self.task_for_comp.replace('sin', 'math.sin')
        self.task_for_comp = self.task_for_comp.replace('cos', 'math.cos')
        self.task_for_comp = self.task_for_comp.replace('tg', 'math.tan')

    # Здесь проходит инициализация всего
    def __initialization_in_level(self):
        self.__init_trigonometric_list()

        # В этой переменной, будет хранится кол-во операндов,
        # которые будут в выражении
        self.count_operands = random.randint(1, 3)

        self.__generate_template_task()

        # После составления шаблона, мы убираем последние 2 символа т.к там может быть
        # случайный оператор
        self.task_for_user = self.task_for_user[0:-2]
        self.task_for_comp = self.task_for_user

    # cr - create, temp - templates, mh - madium and high level
    # Создаем шаблоны для среднего и сложного режима
    def __cr_temp_mh(self, temp_list_arguments):
        for i in range(0, self.count_operands):
            # g_or_r - градусы или радианы. Для разнообразия сред. уровня
            g_or_r = random.randint(1, 2)

            if g_or_r == 1:
                num = self.graduses_list[random.randint(0, self.graduses_list_size)]
                temp_list_arguments.append(str(num))
            elif g_or_r == 2:
                num = self.radian_lists[random.randint(0, self.radian_lists_size - 1)]
                temp_list_arguments.append(str(num))

    # Распределение значений по аргументам
    def __distribution_args_mh(self, temp_list_radians, temp_list_arguments):
        for i in range(0, self.count_operands):
            temp_arg = temp_list_arguments[i]

            temp_arg = temp_arg.replace('π', 'math.pi')
            temp_arg = temp_arg.replace('°', '')
            temp_arg = temp_arg.replace('×', '*')

            # Если нашли ПИ, то это радианная мера (к примеру: π/2, 3π/2), и нужно сделать вычисления
            if temp_arg.find('pi') != -1:
                temp_list_radians.append(round(eval(temp_arg), decimal_places))
            else:
                temp_list_radians.append(round(math.radians(float(temp_arg)), decimal_places))

    # Главная функция по генерации выражений
    def generate_task(self, level):


        # Легкий уровень
        if level == 0:
            # Запись базовых градусов, которые выделены в таблице
            self.graduses_list = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
            self.graduses_list_size = len(self.graduses_list)

            self.__initialization_in_level()

            # Здесь будут хранится временно выбранные градусы
            temp_list_graduses = []
            for i in range(0, self.count_operands):
                gradus = self.graduses_list[random.randint(0, self.graduses_list_size - 1)]
                temp_list_graduses.append(str(gradus) + '°')

            # Форматируем выражение для пользователя
            self.task_for_user = self.task_for_user.format(*temp_list_graduses)

            # Если нашли котангенс, то __replace_ctg
            self.__replace_ctg()

            # Здесь будут хранится конечные радианы. То есть переводим градусы в радианы
            temp_list_radians = []
            for i in range(0, self.count_operands):
                temp_grad = float(temp_list_graduses[i].replace('°', ''))
                temp_radian = math.radians(temp_grad)
                temp_list_radians.append(round(temp_radian, decimal_places))

            # Форматируем выражение для компьютера
            self.task_for_comp = self.task_for_comp.format(*temp_list_radians)

            print (self.task_for_comp)




        # Средний(1) и сложный(2) уровень
        elif level == 1 or level == 2:

            # Средний уровень
            if level == 1:
                for i in range(5, 360, 5):
                    self.graduses_list.append(i)
            # Сложный уровень
            elif level == 2:
                for i in range(1, 720):
                    self.graduses_list.append(i)

            # Здесь происходит все тоже самое, что и в Легком уровне, но есть пару отличий
            self.graduses_list_size = len(self.graduses_list)

            self.__initialization_in_level()

            temp_list_arguments = []
            self.__cr_temp_mh(temp_list_arguments)

            self.task_for_user = self.task_for_user.format(*temp_list_arguments)
            self.__replace_ctg()

            temp_list_radians = []
            # Здесь идет распределение радиан и градусов по аргументам
            self.__distribution_args_mh(temp_list_radians, temp_list_arguments)

            # Форматируем выражение для компьютера
            self.task_for_comp = self.task_for_comp.format(*temp_list_radians)




        self.__change_task_comp()

        self.trigonomentric_funcs.clear()

        return (self.task_for_user, self.task_for_comp)
