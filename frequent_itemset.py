from gui.Ui_freq_itemsets import Ui_FreqItemset
from PyQt5 import QtCore, QtGui, QtWidgets,QtGui
from PyQt5.QtWidgets import QMenuBar, QAction,QDialog,QFileDialog, QComboBox, QCheckBox, QMessageBox
from PyQt5.QtCore import pyqtSlot
from ksdata.apriori_filter import get_last_apriori_filter
from ksdata.itemset_list import get_itemset_list,insert_itemset
class FreqItemset(QDialog, Ui_FreqItemset):
    def __init__(self,connection, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.connection = connection
        self.getLastFilter()
        self.getItemsets()
        self.btnFilterItemset.clicked.connect(self.filter_itemset_click)
    @pyqtSlot()
    def filter_itemset_click(self):
        self.getItemsets()
    def getLastFilter(self):
        record = get_last_apriori_filter(self.connection)
        if record == None:
            self.lblFomDateFilter.setText("")
            self.lblToDateFilter.setText("")
            self.lblMinSupportFilter.setText("")
            self.lblMinConfFilter.setText("")
        else:
            self.lblFomDateFilter.setText((record[0]).strftime("%m/%d/%Y"))
            self.lblToDateFilter.setText((record[1]).strftime("%m/%d/%Y"))
            self.lblMinSupportFilter.setText(format(record[2],'0.4f'))
            self.lblMinConfFilter.setText(format(record[3],'0.2f'))
    def getItemsets(self):
        chk = False
        contain = ''
        if(self.chkShow.isChecked()):
            chk = True
        if len(self.txtFilterContains.text()) > 0:
            contain = self.txtFilterContains.text()
        
        pre_records = get_itemset_list(self.connection,chk,str(self.lblMinSupportFilter.text()),contain)
        if not pre_records == None:
            self.itemsetTableWidget.setRowCount(0)
            for row, record in enumerate(pre_records):
                self.itemsetTableWidget.insertRow(row)
                self.itemsetTableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(record[0])))
                self.itemsetTableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(record[1])))
                self.itemsetTableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(record[2])))
                self.itemsetTableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(record[3])))
    