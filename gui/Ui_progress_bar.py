# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\MITE12\ksapriori\gui\progress_bar.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormProgressBar(object):
    def setupUi(self, FormProgressBar):
        FormProgressBar.setObjectName("FormProgressBar")
        FormProgressBar.resize(448, 82)
        self.progressBar = QtWidgets.QProgressBar(FormProgressBar)
        self.progressBar.setGeometry(QtCore.QRect(30, 20, 391, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(FormProgressBar)
        QtCore.QMetaObject.connectSlotsByName(FormProgressBar)

    def retranslateUi(self, FormProgressBar):
        _translate = QtCore.QCoreApplication.translate
        FormProgressBar.setWindowTitle(_translate("FormProgressBar", "Form"))
