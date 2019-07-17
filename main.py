# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtGui import QFont
from design import Ui_design
import TaskGenerate
import random
import math





class MainWindow(QMainWindow):
    user_result = ''
    comp_result = ''

    decimal_places = 10



    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_design()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.begin)



        self.ui.btnCheckAnswerUser.clicked.connect(self.checkAnswerFromUser)
        self.ui.btnAddPi_1.clicked.connect(self.btnAddPi_1)
        self.ui.btnAddSqrt_1.clicked.connect(self.btnAddSqrt_1)
        self.ui.btnAddPi_2.clicked.connect(self.btnAddPi_2)
        self.ui.btnAddSqrt_2.clicked.connect(self.btnAddSqrt_2)

        self.ui.editLineUserAnswerN.setMaxLength(30)
        self.ui.editLineUserAnswerD.setMaxLength(30)

        self.ui.btnCheckAnswerUser.setEnabled(False)
        self.ui.btnAddPi_1.setEnabled(False)
        self.ui.btnAddPi_2.setEnabled(False)
        self.ui.btnAddSqrt_1.setEnabled(False)
        self.ui.btnAddSqrt_2.setEnabled(False)




    def begin(self):
        self.ui.lbNumerator.setText('')

        self.ui.btnCheckAnswerUser.setEnabled(True)
        self.ui.btnAddPi_1.setEnabled(True)
        self.ui.btnAddPi_2.setEnabled(True)
        self.ui.btnAddSqrt_1.setEnabled(True)
        self.ui.btnAddSqrt_2.setEnabled(True)


        sin_a = self.ui.chBoxSin.isChecked()
        cos_a = self.ui.chBoxCos.isChecked()
        tg_a = self.ui.chBoxTg.isChecked()
        ctg_a = self.ui.chBoxCtg.isChecked()

        if self.ui.cbLevel.currentText() == 'Легкая':

            task_user, task_comp = TaskGenerate.generate_easy_task(sin_a, cos_a, tg_a, ctg_a)

            if task_user == 0 and task_comp == 0:
                self.ui.lbNumerator.setText('Ошибка. Вы не выбрали ни одного пункта.')
                return -1
            else:
                self.ui.lbNumerator.setText(task_user)


            # А потом выбираем любую кнопку, на которой будет правильный ответ
            answer_btn = random.randint(0, 4)

            comp_result = round(eval(task_comp), self.decimal_places)

            # Существуют невозможные решения тригонометрических выражений, и если получили странный ответ
            # (обычно получается больше 100 000), то мы делаем проверку, если полученое значение выше 10,
            # то перегенерируем выражение
            if comp_result < -10.0 or comp_result > 10.0:
                self.begin()
            else:
                self.comp_result = str(comp_result)


    def checkAnswerFromUser(self):
        text_from_user_field_n = self.ui.editLineUserAnswerN.text()
        text_from_user_field_d = self.ui.editLineUserAnswerD.text()

        text_from_user_field_n = text_from_user_field_n.replace('π', 'math.pi')
        text_from_user_field_n = text_from_user_field_n.replace('sqrt', 'math.sqrt')
        text_from_user_field_d = text_from_user_field_d.replace('π', 'math.pi')
        text_from_user_field_d = text_from_user_field_d.replace('sqrt', 'math.sqrt')

        try:

            result = 0.0

            result_n = round(eval(text_from_user_field_n), self.decimal_places)

            if len(text_from_user_field_d) > 0:
                result_d = round(eval(text_from_user_field_d), self.decimal_places)
                result = result_n / result_d
            else:
                result = result_n

            result = round(result, self.decimal_places)

            if float(result) == float(self.comp_result):
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
