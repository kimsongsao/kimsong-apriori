from gui.Ui_association_rules import Ui_AssRules
from PyQt5 import QtCore, QtGui, QtWidgets,QtGui
from PyQt5.QtWidgets import QMenuBar, QAction,QDialog,QFileDialog, QComboBox, QCheckBox, QMessageBox
from PyQt5.QtCore import pyqtSlot
from ksdata.apriori_filter import get_last_apriori_filter
from ksdata.rules_list import get_rules_list
class AssociationRules(QDialog, Ui_AssRules):
    def __init__(self,connection, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.connection = connection
        self.getLastFilter()
        self.getRules()
        self.btnFilterAnt.clicked.connect(self.filter_itemset_click)
    @pyqtSlot()
    def filter_itemset_click(self):
        self.getRules()
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
    def getRules(self):
        # select to list
        records = get_rules_list(self.connection,self.txtFilterContainAnt.text(),self.txtFilterContainConsq.text())
        self.rulesTableWidget.setRowCount(0)
        for row, record in enumerate(records):
            self.rulesTableWidget.insertRow(row)
            self.rulesTableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(record[0])))
            self.rulesTableWidget.setItem(row,1,QtWidgets.QTableWidgetItem('->'))
            self.rulesTableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(record[1])))
            self.rulesTableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(format(record[2],'0.4f')))
            self.rulesTableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(format(record[3],'0.2f')))
    
    