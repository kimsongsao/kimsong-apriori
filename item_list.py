from gui.Ui_item_list import Ui_FormItemList
from PyQt5 import QtCore, QtGui, QtWidgets,QtGui
from PyQt5.QtWidgets import QMenuBar, QAction,QDialog,QFileDialog, QComboBox, QCheckBox, QMessageBox
from PyQt5.QtCore import pyqtSlot
import sys
from xlrd import open_workbook,cellname, xldate_as_tuple
from xlrd.sheet import ctype_text
import collections
import pymssql
import datetime
from ksdata.data_list import get_item_list

class ItemList(QDialog, Ui_FormItemList):
    def __init__(self,connection, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.connection = connection

        header = self.itemListTableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        # Event Handler
        self.btnApplyFilter.clicked.connect(self.apply_filter_clicked)
        # self.getItemList()

    def getItemList(self):
        code = self.txtCode.text()
        label = self.txtLabel.text()
        desc = self.txtDescription.text()
        desc2 = self.txtDescription2.text()
        uom = self.txtUnitMeasure.text()
        price = self.txtUnitPrice.text()
        records = get_item_list(self.connection,code,label,desc,desc2,uom,price)
        if not records == None:
            self.itemListTableWidget.setRowCount(0)
            for row, record in enumerate(records):
                self.itemListTableWidget.insertRow(row)
                self.itemListTableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(record[0])))
                self.itemListTableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(record[1])))
                self.itemListTableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(record[2])))
                self.itemListTableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(record[3])))
                self.itemListTableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(str(record[4])))
                self.itemListTableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(format(record[5],'0.2f')))
    @pyqtSlot()
    def apply_filter_clicked(self):
        self.getItemList()