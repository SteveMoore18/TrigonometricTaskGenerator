# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtGui import QFont
from design import Ui_design
import TaskGenerate
import random
import math

'''
Главный файл
Test PyCharm

'''



class MainWindow(QMainWindow):


    # Сколько знаков будет после запятой
    decimal_places = 10

    denominator = False

    comp_result = 0.0

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_design()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.begin) # Кнопка старта



        self.ui.btnCheckAnswerUser.clicked.connect(self.checkAnswerFromUser) # Кнопка 'Проверка'
        self.ui.btnAddPi_1.clicked.connect(self.btnAddPi_1)                  # Кнопка для добавления ПИ в 1-ое поле пользовательского ответа
        self.ui.btnAddSqrt_1.clicked.connect(self.btnAddSqrt_1)              # Кнопка для добавления корня в 1-ое поле пользовательского ответа
        self.ui.btnAddPi_2.clicked.connect(self.btnAddPi_2)                  # Кнопка для добавления ПИ во 2-ое поле пользовательского ответа
        self.ui.btnAddSqrt_2.clicked.connect(self.btnAddSqrt_2)              # Кнопка для добавления корня во 2-ое поле пользовательского ответа

        self.ui.editLineUserAnswerN.setMaxLength(30)
        self.ui.editLineUserAnswerD.setMaxLength(30)

        # Блокируем кнопки до начала
        self.ui.btnCheckAnswerUser.setEnabled(False)
        self.ui.btnAddPi_1.setEnabled(False)
        self.ui.btnAddPi_2.setEnabled(False)
        self.ui.btnAddSqrt_1.setEnabled(False)
        self.ui.btnAddSqrt_2.setEnabled(False)





    # Начало генерации выражений
    def begin(self):


        self.ui.lbNumerator.setText('')
        self.ui.lbDenominator.setText('')
        self.ui.lbLine.setText('')
        denominator = False

        # Берем значения с QCheckBox, которые выбрал пользователь
        sin_a = self.ui.chBoxSin.isChecked()
        cos_a = self.ui.chBoxCos.isChecked()
        tg_a = self.ui.chBoxTg.isChecked()
        ctg_a = self.ui.chBoxCtg.isChecked()

        generate = TaskGenerate.Generate(sin_a, cos_a, tg_a, ctg_a)



        # Если пользователь ничего не выбрал, то вылазиет ошибка
        if sin_a == False and cos_a == False and tg_a == False and ctg_a == False:
            self.ui.lbNumerator.setText('Ошибка. Вы не выбрали ни одного пункта.')
            return -1

        # Активируем заблокированые кнопки
        self.ui.btnCheckAnswerUser.setEnabled(True)
        self.ui.btnAddPi_1.setEnabled(True)
        self.ui.btnAddPi_2.setEnabled(True)
        self.ui.btnAddSqrt_1.setEnabled(True)
        self.ui.btnAddSqrt_2.setEnabled(True)



        # Если режим "Легкий", то выполняем это условие
        if self.ui.cbLevel.currentText() == 'Легкая':

            task_user, task_comp = generate.generate_task(0)

            self.ui.lbNumerator.setText(task_user)


            comp_result = round(eval(task_comp), self.decimal_places)


            if comp_result < -10.0 or comp_result > 10.0:
                self.begin()
            else:
                self.comp_result = str(comp_result)

        elif self.ui.cbLevel.currentText() == 'Средняя':

            task_user, task_comp = generate.generate_task(1)

            self.ui.lbNumerator.setText(task_user)

            comp_result = round(eval(task_comp), self.decimal_places)


            if comp_result < -10.0 or comp_result > 10.0:
                self.begin()
            else:
                self.comp_result = str(comp_result)



        elif self.ui.cbLevel.currentText() == 'Сложная':
            self.ui.lbLine.setText('———————————————————————')

            generate_d = TaskGenerate.Generate(sin_a, cos_a, tg_a, ctg_a)

            task_user_n, task_comp_n = generate.generate_task(2)
            task_user_d, task_comp_d = generate_d.generate_task(2)

            self.ui.lbNumerator.setText(task_user_n)
            self.ui.lbDenominator.setText(task_user_d)


            comp_result_n = round(eval(task_comp_n), self.decimal_places)
            comp_result_d = round(eval(task_comp_d), self.decimal_places)

            comp_result = round(comp_result_n / comp_result_d, self.decimal_places)

            self.comp_result = comp_result


            '''if comp_result < -10.0 or comp_result > 10.0:
                self.begin()
            else:
                self.comp_result = str(comp_result)'''



    # Если пользователь приготовил ответ, и нажал на кнопку "Проверить", то вызывается эта функция
    def checkAnswerFromUser(self):

        # Текст из числителя QLineEdit
        text_from_user_field_n = self.ui.editLineUserAnswerN.text()

        # Текст из знаменателя QLineEdit
        text_from_user_field_d = self.ui.editLineUserAnswerD.text()

        # Делаем необходимые замены
        text_from_user_field_n = text_from_user_field_n.replace('π', 'math.pi')
        text_from_user_field_n = text_from_user_field_n.replace('sqrt', 'math.sqrt')
        text_from_user_field_d = text_from_user_field_d.replace('π', 'math.pi')
        text_from_user_field_d = text_from_user_field_d.replace('sqrt', 'math.sqrt')

        try:

            # Главный результат от пользователя
            result = 0.0

            # Результат выполнения выражения из числителя
            result_n = round(eval(text_from_user_field_n), self.decimal_places)

            # Если у пользователя есть знаменатель,
            if len(text_from_user_field_d) > 0:
                # То считываем из поля "знаменатель" QLineEdit
                result_d = round(eval(text_from_user_field_d), self.decimal_places)

                # И делим числитель на знаменатель
                result = result_n / result_d
            else:

                # Если знаменателя нет, то просто делаем присваивание
                result = result_n

            result = round(result, self.decimal_places)


            # Сравниваем результаты от пользователя и результаты, которые сделал компьютер
            if float(result) == float(self.comp_result):

                # Если все ОК, то генерируем новый пример и очищаем поля
                self.begin()
                self.ui.editLineUserAnswerD.setText('')
                self.ui.editLineUserAnswerN.setText('')

                self.ui.lbStatus.setText('Ответ верный.')
            else:
                self.ui.lbStatus.setText('Ответ не верный.')

            print (result)
            print (self.comp_result)

        except:
            msg = QMessageBox()
            msg.setText('Ошибка. Проверьте, возможно вы не так ввели значения.')
            msg.exec_()




    def btnAddPi_1(self):
        self.ui.editLineUserAnswerN.insert('π')

    def btnAddSqrt_1(self):
        self.ui.editLineUserAnswerN.insert('sqrt()')


    def btnAddPi_2(self):
        self.ui.editLineUserAnswerD.insert('π')

    def btnAddSqrt_2(self):
        self.ui.editLineUserAnswerD.insert('sqrt()')


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
