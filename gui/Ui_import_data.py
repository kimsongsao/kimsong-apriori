# -*- coding: utf-8 -*-

# Author: Kimsong Sao
# Email: saokimsong@gmail.com
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormImport(object):
    def setupUi(self, FormImport):
        FormImport.setObjectName("FormImport")
        FormImport.resize(697, 606)
        self.btnDoImport = QtWidgets.QPushButton(FormImport)
        self.btnDoImport.setGeometry(QtCore.QRect(610, 570, 75, 23))
        self.btnDoImport.setObjectName("btnDoImport")
        self.layoutWidget = QtWidgets.QWidget(FormImport)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 23, 671, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lblFilePath = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblFilePath.setFont(font)
        self.lblFilePath.setObjectName("lblFilePath")
        self.verticalLayout.addWidget(self.lblFilePath)
        self.lblSQLServerIP = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblSQLServerIP.setFont(font)
        self.lblSQLServerIP.setObjectName("lblSQLServerIP")
        self.verticalLayout.addWidget(self.lblSQLServerIP)
        self.lblMySQLPort = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblMySQLPort.setFont(font)
        self.lblMySQLPort.setObjectName("lblMySQLPort")
        self.verticalLayout.addWidget(self.lblMySQLPort)
        self.lblSQlServerAuth = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblSQlServerAuth.setFont(font)
        self.lblSQlServerAuth.setObjectName("lblSQlServerAuth")
        self.verticalLayout.addWidget(self.lblSQlServerAuth)
        self.lblSQLServerUserName = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblSQLServerUserName.setFont(font)
        self.lblSQLServerUserName.setObjectName("lblSQLServerUserName")
        self.verticalLayout.addWidget(self.lblSQLServerUserName)
        self.lblSQLServerPassword = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblSQLServerPassword.setFont(font)
        self.lblSQLServerPassword.setObjectName("lblSQLServerPassword")
        self.verticalLayout.addWidget(self.lblSQLServerPassword)
        self.lblSQLServerDatabase = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblSQLServerDatabase.setFont(font)
        self.lblSQLServerDatabase.setObjectName("lblSQLServerDatabase")
        self.verticalLayout.addWidget(self.lblSQLServerDatabase)
        self.lblWebAPIURL = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblWebAPIURL.setFont(font)
        self.lblWebAPIURL.setObjectName("lblWebAPIURL")
        self.verticalLayout.addWidget(self.lblWebAPIURL)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.lblTargetTable = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblTargetTable.setFont(font)
        self.lblTargetTable.setObjectName("lblTargetTable")
        self.verticalLayout.addWidget(self.lblTargetTable)
        self.lblSourceTable = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblSourceTable.setFont(font)
        self.lblSourceTable.setObjectName("lblSourceTable")
        self.verticalLayout.addWidget(self.lblSourceTable)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cboFileType = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.cboFileType.setFont(font)
        self.cboFileType.setObjectName("cboFileType")
        self.cboFileType.addItem("")
        self.cboFileType.addItem("")
        self.cboFileType.addItem("")
        self.cboFileType.addItem("")
        self.cboFileType.addItem("")
        self.cboFileType.addItem("")
        self.verticalLayout_2.addWidget(self.cboFileType)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtImportPath = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.txtImportPath.setFont(font)
        self.txtImportPath.setObjectName("txtImportPath")
        self.horizontalLayout_2.addWidget(self.txtImportPath)
        self.btnImport = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.btnImport.setFont(font)
        self.btnImport.setObjectName("btnImport")
        self.horizontalLayout_2.addWidget(self.btnImport)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtSQLServerIP = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.txtSQLServerIP.setFont(font)
        self.txtSQLServerIP.setObjectName("txtSQLServerIP")
        self.horizontalLayout.addWidget(self.txtSQLServerIP)
        self.btnSQLServerTest = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.btnSQLServerTest.setFont(font)
        self.btnSQLServerTest.setObjectName("btnSQLServerTest")
        self.horizontalLayout.addWidget(self.btnSQLServerTest)
        self.btnSQLServerSave = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.btnSQLServerSave.setFont(font)
        self.btnSQLServerSave.setObjectName("btnSQLServerSave")
        self.horizontalLayout.addWidget(self.btnSQLServerSave)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.txtMySQLPort = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.txtMySQLPort.setFont(font)
        self.txtMySQLPort.setObjectName("txtMySQLPort")
        self.verticalLayout_2.addWidget(self.txtMySQLPort)
        self.cboSQLServerAuth = QtWidgets.QComboBox(self.layoutWidget)
        self.cboSQLServerAuth.setObjectName("cboSQLServerAuth")
        self.cboSQLServerAuth.addItem("")
        self.cboSQLServerAuth.addItem("")
        self.verticalLayout_2.addWidget(self.cboSQLServerAuth)
        self.txtSQLServerUserName = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.txtSQLServerUserName.setFont(font)
        self.txtSQLServerUserName.setObjectName("txtSQLServerUserName")
        self.verticalLayout_2.addWidget(self.txtSQLServerUserName)
        self.txtSQLServerPassword = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.txtSQLServerPassword.setFont(font)
        self.txtSQLServerPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtSQLServerPassword.setObjectName("txtSQLServerPassword")
        self.verticalLayout_2.addWidget(self.txtSQLServerPassword)
        self.txtSQLServerDatabase = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.txtSQLServerDatabase.setFont(font)
        self.txtSQLServerDatabase.setObjectName("txtSQLServerDatabase")
        self.verticalLayout_2.addWidget(self.txtSQLServerDatabase)
        self.txtWebAPIURL = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.txtWebAPIURL.setFont(font)
        self.txtWebAPIURL.setObjectName("txtWebAPIURL")
        self.verticalLayout_2.addWidget(self.txtWebAPIURL)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.cboTargetTable = QtWidgets.QComboBox(self.layoutWidget)
        self.cboTargetTable.setObjectName("cboTargetTable")
        self.cboTargetTable.addItem("")
        self.cboTargetTable.setItemText(0, "")
        self.cboTargetTable.addItem("")
        self.cboTargetTable.addItem("")
        self.verticalLayout_2.addWidget(self.cboTargetTable)
        self.cboSourceTable = QtWidgets.QComboBox(self.layoutWidget)
        self.cboSourceTable.setObjectName("cboSourceTable")
        self.verticalLayout_2.addWidget(self.cboSourceTable)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.matchFieldsTableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.matchFieldsTableWidget.setObjectName("matchFieldsTableWidget")
        self.matchFieldsTableWidget.setColumnCount(3)
        self.matchFieldsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.matchFieldsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.matchFieldsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.matchFieldsTableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_3.addWidget(self.matchFieldsTableWidget)

        self.retranslateUi(FormImport)
        QtCore.QMetaObject.connectSlotsByName(FormImport)

    def retranslateUi(self, FormImport):
        _translate = QtCore.QCoreApplication.translate
        FormImport.setWindowTitle(_translate("FormImport", "Form"))
        self.btnDoImport.setText(_translate("FormImport", "Import"))
        self.label_3.setText(_translate("FormImport", "Select Source Type"))
        self.lblFilePath.setText(_translate("FormImport", "File Path"))
        self.lblSQLServerIP.setText(_translate("FormImport", "Host Name/IP Address"))
        self.lblMySQLPort.setText(_translate("FormImport", "Port"))
        self.lblSQlServerAuth.setText(_translate("FormImport", "Authentication"))
        self.lblSQLServerUserName.setText(_translate("FormImport", "User Name"))
        self.lblSQLServerPassword.setText(_translate("FormImport", "Password"))
        self.lblSQLServerDatabase.setText(_translate("FormImport", "Database Name"))
        self.lblWebAPIURL.setText(_translate("FormImport", "URL"))
        self.lblTargetTable.setText(_translate("FormImport", "Target Table"))
        self.lblSourceTable.setText(_translate("FormImport", "Source Table"))
        self.cboFileType.setItemText(0, _translate("FormImport", "Excel file (2007 or later) (*.xlsx)"))
        self.cboFileType.setItemText(1, _translate("FormImport", "CSV file (*.csv)"))
        self.cboFileType.setItemText(2, _translate("FormImport", "Microsoft SQL Server"))
        self.cboFileType.setItemText(3, _translate("FormImport", "MySQL"))
        self.cboFileType.setItemText(4, _translate("FormImport", "REST Api"))
        self.cboFileType.setItemText(5, _translate("FormImport", "Oracle"))
        self.btnImport.setText(_translate("FormImport", "..."))
        self.btnSQLServerTest.setText(_translate("FormImport", "Test Connection"))
        self.btnSQLServerSave.setText(_translate("FormImport", "Save"))
        self.cboSQLServerAuth.setItemText(0, _translate("FormImport", "SQL Server Authentication"))
        self.cboSQLServerAuth.setItemText(1, _translate("FormImport", "Windows Authentication"))
        self.cboTargetTable.setItemText(1, _translate("FormImport", "Item"))
        self.cboTargetTable.setItemText(2, _translate("FormImport", "Sales Transaction"))
        item = self.matchFieldsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FormImport", "Target Field"))
        item = self.matchFieldsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FormImport", "Source Field"))