# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/design.ui',
# licensing of 'res/design.ui' applies.
#
# Created: Sat Jul 20 11:30:33 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import res
class Ui_design(object):
    def setupUi(self, design):
        design.setObjectName("design")
        design.resize(835, 594)
        design.setStyleSheet("background-color: #ececec;")
        self.centralwidget = QtWidgets.QWidget(design)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 59, 211, 461))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    background-color: #e2e2e2;\n"
"    border: 1px solid #d3d3d3;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.cbLevel = QtWidgets.QComboBox(self.groupBox)
        self.cbLevel.setGeometry(QtCore.QRect(10, 60, 191, 31))
        self.cbLevel.setStyleSheet("QComboBox\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #a9a9a9;\n"
"    border-radius: 5px;\n"
"    border-bottom-left-radius: 1px; \n"
"    border-top-left-radius: 1px; \n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable\n"
"{\n"
"    selection-background-color: #1081ff;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QComboBox:drop-down\n"
"{\n"
"    width: 20px;\n"
"    background-color: #1081ff;\n"
"    border-left-width: 2px;\n"
"    border-bottom-right-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    border-left-color: #1081ff;\n"
"    border-left-style: solid;\n"
"}\n"
"\n"
"QComboBox:down-arrow\n"
"{\n"
"    padding-right: 2px;\n"
"    image: url(:/images/arrow_down.png)\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #a9a9a9;\n"
"    border-radius: 6px;\n"
"}")
        self.cbLevel.setObjectName("cbLevel")
        self.cbLevel.addItem("")
        self.cbLevel.addItem("")
        self.cbLevel.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: #e2e2e2;")
        self.label_2.setObjectName("label_2")
        self.chBoxSin = QtWidgets.QCheckBox(self.groupBox)
        self.chBoxSin.setGeometry(QtCore.QRect(10, 110, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chBoxSin.setFont(font)
        self.chBoxSin.setStyleSheet("QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    background-color: #e2e2e2;\n"
"}\n"
"\n"
"QCheckBox:indicator\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #a5a5a5;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QCheckBox:indicator:hover\n"
"{\n"
"    background-color: #ececec;\n"
"    border: 1px solid #a5a5a5;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QCheckBox:indicator:checked\n"
"{\n"
"    image: url(:/images/check.png);\n"
"    background-color: #3b99fd;\n"
"    border: 1px solid #2c90fc;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QCheckBox:indicator:checked:hover\n"
"{\n"
"    image: url(:/images/check.png);\n"
"    background-color: #208bf9;\n"
"    border: 1px solid #2c90fc;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"\n"
"")
        self.chBoxSin.setChecked(True)
        self.chBoxSin.setObjectName("chBoxSin")
        self.chBoxCos = QtWidgets.QCheckBox(self.groupBox)
        self.chBoxCos.setGeometry(QtCore.QRect(10, 140, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chBoxCos.setFont(font)
        self.chBoxCos.setStyleSheet("QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    background-color: #e2e2e2;\n"
"}\n"
"\n"
"QCheckBox:indicator\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #a5a5a5;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QCheckBox:indicator:hover\n"
"{\n"
"    background-color: #ececec;\n"
"    border: 1px solid #a5a5a5;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QCheckBox:indicator:checked\n"
"{\n"
"    image: url(:/images/check.png);\n"
"    background-color: #3b99fd;\n"
"    border: 1px solid #2c90fc;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QCheckBox:indicator:checked:hover\n"
"{\n"
"    image: url(:/images/check.png);\n"
"    background-color: #208bf9;\n"
"    border: 1px solid #2c90fc;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"\n"
"")
        self.chBoxCos.setChecked(True)
        self.chBoxCos.setObjectName("chBoxCos")
        self.chBoxTg = QtWidgets.QCheckBox(self.groupBox)
        self.chBoxTg.setGeometry(QtCore.QRect(10, 170, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chBoxTg.setFont(font)
        self.chBoxTg.setStyleSheet("QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    background-color: #e2e2e2;\n"
"}\n"
"\n"
"QCheckBox:indicator\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #a5a5a5;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QCheckBox:indicator:hover\n"
"{\n"
"    background-color: #ececec;\n"
"    border: 1px solid #a5a5a5;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QCheckBox:indicator:checked\n"
"{\n"
"    image: url(:/images/check.png);\n"
"    background-color: #3b99fd;\n"
"    border: 1px solid #2c90fc;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QCheckBox:indicator:checked:hover\n"
"{\n"
"    image: url(:/images/check.png);\n"
"    background-color: #208bf9;\n"
"    border: 1px solid #2c90fc;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"\n"
"")
        self.chBoxTg.setChecked(True)
        self.chBoxTg.setObjectName("chBoxTg")
        self.chBoxCtg = QtWidgets.QCheckBox(self.groupBox)
        self.chBoxCtg.setGeometry(QtCore.QRect(10, 200, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chBoxCtg.setFont(font)
        self.chBoxCtg.setStyleSheet("QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    background-color: #e2e2e2;\n"
"}\n"
"\n"
"QCheckBox:indicator\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #a5a5a5;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QCheckBox:indicator:hover\n"
"{\n"
"    background-color: #ececec;\n"
"    border: 1px solid #a5a5a5;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QCheckBox:indicator:checked\n"
"{\n"
"    image: url(:/images/check.png);\n"
"    background-color: #3b99fd;\n"
"    border: 1px solid #2c90fc;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QCheckBox:indicator:checked:hover\n"
"{\n"
"    image: url(:/images/check.png);\n"
"    background-color: #208bf9;\n"
"    border: 1px solid #2c90fc;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"\n"
"")
        self.chBoxCtg.setChecked(True)
        self.chBoxCtg.setObjectName("chBoxCtg")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 260, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #bfbfbf;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(238, 238, 236);\n"
"    border: 1px solid #bfbfbf;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #1786fe;\n"
"    color: white;\n"
"    border: 1px solid #4ca2f9;\n"
"    border-radius: 5px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lbNumerator = QtWidgets.QLabel(self.centralwidget)
        self.lbNumerator.setGeometry(QtCore.QRect(260, 90, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbNumerator.setFont(font)
        self.lbNumerator.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lbNumerator.setObjectName("lbNumerator")
        self.lbLine = QtWidgets.QLabel(self.centralwidget)
        self.lbLine.setGeometry(QtCore.QRect(260, 120, 501, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbLine.setFont(font)
        self.lbLine.setStyleSheet("")
        self.lbLine.setText("")
        self.lbLine.setObjectName("lbLine")
        self.lbDenominator = QtWidgets.QLabel(self.centralwidget)
        self.lbDenominator.setGeometry(QtCore.QRect(260, 140, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbDenominator.setFont(font)
        self.lbDenominator.setText("")
        self.lbDenominator.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbDenominator.setObjectName("lbDenominator")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 200, 531, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"    background-color: #e2e2e2;\n"
"    border: 1px solid #d3d3d3;\n"
"    border-radius: 4px;\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.editLineUserAnswerN = QtWidgets.QLineEdit(self.groupBox_2)
        self.editLineUserAnswerN.setGeometry(QtCore.QRect(130, 40, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editLineUserAnswerN.setFont(font)
        self.editLineUserAnswerN.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #a9a9a9;\n"
"}\n"
"\n"
"\n"
"")
        self.editLineUserAnswerN.setText("")
        self.editLineUserAnswerN.setObjectName("editLineUserAnswerN")
        self.btnCheckAnswerUser = QtWidgets.QPushButton(self.groupBox_2)
        self.btnCheckAnswerUser.setGeometry(QtCore.QRect(130, 120, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCheckAnswerUser.setFont(font)
        self.btnCheckAnswerUser.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #bfbfbf;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(238, 238, 236);\n"
"    border: 1px solid #bfbfbf;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #1786fe;\n"
"    color: white;\n"
"    border: 1px solid #4ca2f9;\n"
"    border-radius: 5px;\n"
"}")
        self.btnCheckAnswerUser.setObjectName("btnCheckAnswerUser")
        self.btnAddSqrt_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btnAddSqrt_2.setGeometry(QtCore.QRect(340, 80, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAddSqrt_2.setFont(font)
        self.btnAddSqrt_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #bfbfbf;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(238, 238, 236);\n"
"    border: 1px solid #bfbfbf;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #1786fe;\n"
"    color: white;\n"
"    border: 1px solid #4ca2f9;\n"
"    border-radius: 5px;\n"
"}")
        self.btnAddSqrt_2.setObjectName("btnAddSqrt_2")
        self.btnAddPi_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btnAddPi_2.setGeometry(QtCore.QRect(300, 80, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAddPi_2.setFont(font)
        self.btnAddPi_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #bfbfbf;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(238, 238, 236);\n"
"    border: 1px solid #bfbfbf;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #1786fe;\n"
"    color: white;\n"
"    border: 1px solid #4ca2f9;\n"
"    border-radius: 5px;\n"
"}")
        self.btnAddPi_2.setObjectName("btnAddPi_2")
        self.editLineUserAnswerD = QtWidgets.QLineEdit(self.groupBox_2)
        self.editLineUserAnswerD.setGeometry(QtCore.QRect(130, 80, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editLineUserAnswerD.setFont(font)
        self.editLineUserAnswerD.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #a9a9a9;\n"
"}\n"
"\n"
"\n"
"")
        self.editLineUserAnswerD.setObjectName("editLineUserAnswerD")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 511, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: #e2e2e2;")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: #e2e2e2;")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: #e2e2e2;")
        self.label_5.setObjectName("label_5")
        self.btnAddPi_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.btnAddPi_1.setGeometry(QtCore.QRect(300, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAddPi_1.setFont(font)
        self.btnAddPi_1.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #bfbfbf;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(238, 238, 236);\n"
"    border: 1px solid #bfbfbf;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #1786fe;\n"
"    color: white;\n"
"    border: 1px solid #4ca2f9;\n"
"    border-radius: 5px;\n"
"}")
        self.btnAddPi_1.setObjectName("btnAddPi_1")
        self.btnAddSqrt_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.btnAddSqrt_1.setGeometry(QtCore.QRect(340, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAddSqrt_1.setFont(font)
        self.btnAddSqrt_1.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #bfbfbf;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(238, 238, 236);\n"
"    border: 1px solid #bfbfbf;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #1786fe;\n"
"    color: white;\n"
"    border: 1px solid #4ca2f9;\n"
"    border-radius: 5px;\n"
"}")
        self.btnAddSqrt_1.setObjectName("btnAddSqrt_1")
        self.lbStatus = QtWidgets.QLabel(self.groupBox_2)
        self.lbStatus.setGeometry(QtCore.QRect(300, 120, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbStatus.setFont(font)
        self.lbStatus.setStyleSheet("background-color: #e2e2e2;")
        self.lbStatus.setText("")
        self.lbStatus.setObjectName("lbStatus")
        design.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(design)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 22))
        self.menubar.setObjectName("menubar")
        design.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(design)
        self.statusbar.setObjectName("statusbar")
        design.setStatusBar(self.statusbar)

        self.retranslateUi(design)
        QtCore.QMetaObject.connectSlotsByName(design)

    def retranslateUi(self, design):
        design.setWindowTitle(QtWidgets.QApplication.translate("design", "Генератор тригонометрических выражений", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("design", "Генератор задач по тригонометрии", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("design", "Настройки", None, -1))
        self.cbLevel.setItemText(0, QtWidgets.QApplication.translate("design", "Легкая", None, -1))
        self.cbLevel.setItemText(1, QtWidgets.QApplication.translate("design", "Средняя", None, -1))
        self.cbLevel.setItemText(2, QtWidgets.QApplication.translate("design", "Сложная", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("design", "Сложность", None, -1))
        self.chBoxSin.setText(QtWidgets.QApplication.translate("design", "sin(α)", None, -1))
        self.chBoxCos.setText(QtWidgets.QApplication.translate("design", "cos(α)", None, -1))
        self.chBoxTg.setText(QtWidgets.QApplication.translate("design", "tg(α)", None, -1))
        self.chBoxCtg.setText(QtWidgets.QApplication.translate("design", "ctg(α)", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("design", "Начать", None, -1))
        self.lbNumerator.setText(QtWidgets.QApplication.translate("design", "Нажмите на кнопку \'Начать\'", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("design", "Ваш ответ", None, -1))
        self.btnCheckAnswerUser.setText(QtWidgets.QApplication.translate("design", "Проверить", None, -1))
        self.btnAddSqrt_2.setText(QtWidgets.QApplication.translate("design", "√", None, -1))
        self.btnAddPi_2.setText(QtWidgets.QApplication.translate("design", "π", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("design", "Если используете корень, то нажмите на кнопку \'√\' и появится sqrt(), \n"
"а в скобках пишите значение корня", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("design", "Числитель:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("design", "Знаменатель:", None, -1))
        self.btnAddPi_1.setText(QtWidgets.QApplication.translate("design", "π", None, -1))
        self.btnAddSqrt_1.setText(QtWidgets.QApplication.translate("design", "√", None, -1))

