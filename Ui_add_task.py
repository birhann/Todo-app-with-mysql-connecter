# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Lenovo\Desktop\Python\Programlar\Todo App\add_task.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_task(object):
    def setupUi(self, add_task):
        add_task.setObjectName("add_task")
        add_task.resize(634, 500)
        add_task.setMinimumSize(QtCore.QSize(580, 500))
        add_task.setMaximumSize(QtCore.QSize(800, 482))
        self.centralwidget = QtWidgets.QWidget(add_task)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(7, -1, -1, -1)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(300, 30))
        self.label.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.txt_task_title = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_task_title.setMinimumSize(QtCore.QSize(350, 60))
        self.txt_task_title.setMaximumSize(QtCore.QSize(800, 60))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(16)
        self.txt_task_title.setFont(font)
        self.txt_task_title.setObjectName("txt_task_title")
        self.verticalLayout_4.addWidget(self.txt_task_title)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(300, 30))
        self.label_2.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.txt_task_detail = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_task_detail.setMinimumSize(QtCore.QSize(350, 250))
        self.txt_task_detail.setMaximumSize(QtCore.QSize(800, 280))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.txt_task_detail.setFont(font)
        self.txt_task_detail.setObjectName("txt_task_detail")
        self.verticalLayout_5.addWidget(self.txt_task_detail)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 0, 7, 0)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(180, 20))
        self.label_4.setMaximumSize(QtCore.QSize(180, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.start_time = QtWidgets.QDateEdit(self.centralwidget)
        self.start_time.setMinimumSize(QtCore.QSize(180, 50))
        self.start_time.setMaximumSize(QtCore.QSize(180, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_time.setFont(font)
        self.start_time.setObjectName("start_time")
        self.verticalLayout_2.addWidget(self.start_time)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(180, 20))
        self.label_6.setMaximumSize(QtCore.QSize(180, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.end_time = QtWidgets.QDateEdit(self.centralwidget)
        self.end_time.setMinimumSize(QtCore.QSize(180, 50))
        self.end_time.setMaximumSize(QtCore.QSize(180, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.end_time.setFont(font)
        self.end_time.setObjectName("end_time")
        self.verticalLayout_2.addWidget(self.end_time)
        self.important_level = QtWidgets.QComboBox(self.centralwidget)
        self.important_level.setMinimumSize(QtCore.QSize(180, 50))
        self.important_level.setMaximumSize(QtCore.QSize(180, 50))
        self.important_level.setObjectName("important_level")
        self.important_level.addItem("")
        self.important_level.setItemText(0, "Çok Önemli")
        self.important_level.addItem("")
        self.important_level.addItem("")
        self.important_level.addItem("")
        self.verticalLayout_2.addWidget(self.important_level)
        self.btn_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ekle.setMinimumSize(QtCore.QSize(0, 110))
        self.btn_ekle.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("MingLiU_HKSCS-ExtB")
        font.setPointSize(28)
        self.btn_ekle.setFont(font)
        self.btn_ekle.setObjectName("btn_ekle")
        self.verticalLayout_2.addWidget(self.btn_ekle)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        add_task.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(add_task)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 26))
        self.menubar.setObjectName("menubar")
        add_task.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(add_task)
        self.statusbar.setObjectName("statusbar")
        add_task.setStatusBar(self.statusbar)

        self.retranslateUi(add_task)
        QtCore.QMetaObject.connectSlotsByName(add_task)

    def retranslateUi(self, add_task):
        _translate = QtCore.QCoreApplication.translate
        add_task.setWindowTitle(_translate("add_task", "Görev Ekle"))
        self.label.setText(_translate("add_task", "KONU BAŞLIĞI"))
        self.txt_task_title.setText(_translate("add_task", "Deneme"))
        self.label_2.setText(_translate("add_task", "KONU İÇERİĞİ"))
        self.txt_task_detail.setPlainText(_translate("add_task", "BİR GÜN BİR GÜN BİR ÇOCUK EVE DE BAKMIŞ KİMSE YOK"))
        self.label_4.setText(_translate("add_task", "Başlangıç Tarihi"))
        self.label_6.setText(_translate("add_task", "Bitiş Tarihi"))
        self.important_level.setCurrentText(_translate("add_task", "Çok Önemli"))
        self.important_level.setItemText(1, _translate("add_task", "Önemli"))
        self.important_level.setItemText(2, _translate("add_task", "Önemsiz"))
        self.important_level.setItemText(3, _translate("add_task", "Çok Önemsiz"))
        self.btn_ekle.setText(_translate("add_task", "EKLE"))

