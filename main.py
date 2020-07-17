import sys
from ksdata.database import create_open_database
from ksdata.apriori_filter import get_last_apriori_filter
from ksdata.itemset_list import get_itemset_list,insert_itemset
from ksdata.rules_list import get_rules_list,insert_rule
from ksdata.activity_log import insert_activity_log
from ksdata.preprocessing import generate_preprocessing
from ksdata.apriori_filter import insert_apriori_filter
from ksapriori.load_data import load_dataset
from ksapriori.apriori import ksapriori
from ksapriori.association_rule import generate_rule
# ===============
from PyQt5 import QtCore, QtGui, QtWidgets,QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMenuBar, QAction,QDialog,QFileDialog, QComboBox,QApplication,QPushButton,QMessageBox

from gui.Ui_main import Ui_MainWindow
from import_data import ImportData
from frequent_itemset import FreqItemset
from association_rules import AssociationRules
from item_list import ItemList
from datetime import datetime, date
import time

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.showMaximized()

        self.ui.txtFromDate.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.txtFromDate.setCalendarPopup(True)
        self.ui.txtToDate.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.txtToDate.setCalendarPopup(True)
        # init connection
        self.connection = create_open_database(host='localhost',port=3307,user='root',password='blue123',db_name='ext_5000_01')
        # source_item_columns = []
        # target_item_columns = []
        # path = 'C:\\Users\\Kimsong\\Desktop\\Online Retail.xlsx'
        # result = import_from_excel(path,'Online Retail',source_item_columns,target_item_columns,connection)
        header = self.ui.itemsetTableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Interactive)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        header1 = self.ui.rulesTableWidget.horizontalHeader()       
        header1.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header1.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        # end test connection
        # create event handlermenuImport_Data
        self.ui.actionImport_Data.triggered.connect(self.import_option_click)
        self.ui.actionFreq_Itemset.triggered.connect(self.freq_itemset_click)
        self.ui.actionAssociation_Rules_2.triggered.connect(self.association_rules_click)
        self.ui.actionItem_List.triggered.connect(self.item_list_click)
        self.ui.btnRunApriori.clicked.connect(self.run_apriori_click)
        self.ui.btnFilterItemset.clicked.connect(self.filter_itemset_click)
        # self.ui.chkShow.clicked.connect(self.show_checked)
        self.ui.btnFilterAnt.clicked.connect(self.filter_ant_click)
        self.ui.btnFilterConseq.clicked.connect(self.filter_conseq_click)
        # end create event handler
        self.getLastFilter()
        self.getItemsets()
        self.getRules() 
    def getLastFilter(self):
        record = get_last_apriori_filter(self.connection)
        if record == None:
            self.ui.lblFomDateFilter.setText("")
            self.ui.lblToDateFilter.setText("")
            self.ui.lblMinSupportFilter.setText("")
            self.ui.lblMinConfFilter.setText("")
        else:
            self.ui.lblFomDateFilter.setText((record[0]).strftime("%m/%d/%Y"))
            self.ui.lblToDateFilter.setText((record[1]).strftime("%m/%d/%Y"))
            self.ui.lblMinSupportFilter.setText(format(record[2],'0.4f'))
            self.ui.lblMinConfFilter.setText(format(record[3],'0.2f'))
    def getItemsets(self):
        chk = False
        contain = ''
        if(self.ui.chkShow.isChecked()):
            chk = True
        if len(self.ui.txtFilterContains.text()) > 0:
            contain = self.ui.txtFilterContains.text()
        
        pre_records = get_itemset_list(self.connection,chk,str(self.ui.lblMinSupportFilter.text()),contain)
        if not pre_records == None:
            self.ui.itemsetTableWidget.setRowCount(0)
            for row, record in enumerate(pre_records):
                self.ui.itemsetTableWidget.insertRow(row)
                self.ui.itemsetTableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(record[0])))
                self.ui.itemsetTableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(record[1])))
                self.ui.itemsetTableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(record[2])))
                self.ui.itemsetTableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(record[3])))
    def getRules(self):
        # select to list
        records = get_rules_list(self.connection,self.ui.txtFilterContainAnt.text(),self.ui.txtFilterContainConsq.text())
        self.ui.rulesTableWidget.setRowCount(0)
        for row, record in enumerate(records):
            self.ui.rulesTableWidget.insertRow(row)
            self.ui.rulesTableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(record[0])))
            self.ui.rulesTableWidget.setItem(row,1,QtWidgets.QTableWidgetItem('->'))
            self.ui.rulesTableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(record[1])))
            self.ui.rulesTableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(format(record[2],'0.4f')))
            self.ui.rulesTableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(format(record[3],'0.2f')))
    @pyqtSlot()
    def import_option_click(self):
        self.importForm = ImportData(self.connection)
        self.importForm.show()
    @pyqtSlot()
    def freq_itemset_click(self):
        self.freq = FreqItemset(self.connection)
        self.freq.show()
    @pyqtSlot()
    def association_rules_click(self):
        self.asss = AssociationRules(self.connection)
        self.asss.show()
    @pyqtSlot()
    def item_list_click(self):
        self.items = ItemList(self.connection)
        self.items.show()
    @pyqtSlot()
    def run_apriori_click(self):
        try:
            from_date = self.ui.txtFromDate.date()
            from_date = from_date.toPyDate()
            to_date = self.ui.txtToDate.date()
            to_date = to_date.toPyDate()
            min_support = self.ui.minSupportSpinBox.value()
            min_confidence = self.ui.minConfSpinBox.value()
            # preprocessing
            start_time = datetime.now()
            total_tran = generate_preprocessing(self.connection,from_date,to_date)
            # print("Trans : " + str(total_tran))
            filter_id = insert_apriori_filter(self.connection,from_date,to_date,min_support,min_confidence,total_tran)
            end_time = datetime.now()
            insert_activity_log(self.connection,filter_id,'matching',start_time,end_time)
            self.connection.commit()
            # start generate itemsets
            start_time = datetime.now()
            dataset = load_dataset(self.connection)
            # generating
            frequent_itemsets,support_data = ksapriori(dataset,min_support)
            end_time = datetime.now()
            insert_activity_log(self.connection,filter_id,'generate_itemset',start_time,end_time)
            insert_itemset(self.connection,support_data,total_tran)
            # self.connection.commit()
            # Generating rules
            start_time = datetime.now()
            rule_list = generate_rule(frequent_itemsets,support_data,min_confidence)
            # print(rule_list)
            end_time = datetime.now()
            insert_activity_log(self.connection,filter_id,'generate_rules',start_time,end_time)
            insert_rule(self.connection,rule_list)
            self.connection.commit()
            # connection.close()
            self.getLastFilter()
            self.getItemsets()
            self.getRules()
        except Exception as e:
            print(str(e))
            QMessageBox.warning(None,'Recommendation System',str(e))
    @pyqtSlot()
    def filter_itemset_click(self):
        self.getItemsets()
    @pyqtSlot()
    def filter_ant_click(self):
        self.getRules()
    @pyqtSlot()
    def filter_conseq_click(self):
        self.getRules()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    sys.exit(app.exec_())
    