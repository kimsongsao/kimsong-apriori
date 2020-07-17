from gui.Ui_import_data import Ui_FormImport
from PyQt5 import QtCore, QtGui, QtWidgets,QtGui
from PyQt5.QtWidgets import QMenuBar, QAction,QDialog,QFileDialog, QComboBox, QCheckBox, QMessageBox
from PyQt5.QtCore import pyqtSlot
import sys
from xlrd import open_workbook,cellname, xldate_as_tuple
from xlrd.sheet import ctype_text
import collections
import pymssql
import datetime
from ksdata.import_item import import_item_from_excel,import_item_from_sqlserver
from ksdata.import_sales import import_sales_from_excel,import_sales_from_sqlserver
from ksdata.database import create_open_database
from ksdata.activity_log import insert_activity_log
class ImportData(QDialog, Ui_FormImport):
    def __init__(self,connection, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        header = self.matchFieldsTableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.btnImport.clicked.connect(self.browse_import_file_clicked)
        self.cboFileType.currentTextChanged.connect(self.on_cbo_file_type_changed)
        self.cboTargetTable.currentTextChanged.connect(self.on_cbo_target_table_changed)
        self.cboSourceTable.currentTextChanged.connect(self.on_cbo_source_table_changed)
        self.btnDoImport.clicked.connect(self.on_do_import_clicked)
        self.cboSQLServerAuth.currentTextChanged.connect(self.on_cbo_sql_server_auth_changed)
        self.btnSQLServerTest.clicked.connect(self.on_server_test_connection_clicked)
        self.btnSQLServerSave.clicked.connect(self.on_server_save_connection_clicked)
        self.hideControls(0)
        self.connection = connection # create_open_database(host='localhost',port=3307,user='root',password='blue123',db_name='ksoft')
        # print(self.connection)
    def hideControls(self,type_import):
        """
        Argurments:
            type_import
                - 0 : Microsoft Ecel
                - 1 : CSV Files
                - 2 : Microsoft SQL Server
                - 3 : MySQL Server
                - 4 : REST Web Application Interface (API)
                - 5 : Oracle Server

        """
        if type_import == 0:
            self.lblSourceTable.show()
            self.lblTargetTable.show()
            self.cboSourceTable.show()
            self.cboTargetTable.show()
            self.lblFilePath.show()
            self.txtImportPath.show()
            self.btnImport.show()

            # hide others
            self.lblSQLServerIP.hide()
            self.txtSQLServerIP.hide()
            self.lblSQlServerAuth.hide()
            self.cboSQLServerAuth.hide()
            self.lblSQLServerUserName.hide()
            self.txtSQLServerUserName.hide()
            self.lblSQLServerPassword.hide()
            self.txtSQLServerPassword.hide()
            self.lblMySQLPort.hide()
            self.txtMySQLPort.hide()
            self.btnSQLServerTest.hide()
            self.btnSQLServerSave.hide()
            self.lblWebAPIURL.hide()
            self.txtWebAPIURL.hide()
            self.lblSQLServerDatabase.hide()
            self.txtSQLServerDatabase.hide()
        elif type_import == 1:
            print('next ....')
        elif type_import == 2:
            self.lblSQLServerIP.show()
            self.txtSQLServerIP.show()
            self.lblSQlServerAuth.show()
            self.cboSQLServerAuth.show()
            self.lblSQLServerUserName.show()
            self.txtSQLServerUserName.show()
            self.lblSQLServerPassword.show()
            self.txtSQLServerPassword.show()
            self.btnSQLServerTest.show()
            self.btnSQLServerSave.show()
            self.lblSQLServerDatabase.show()
            self.txtSQLServerDatabase.show()
            # Testing Purpose
            self.txtSQLServerIP.setText('kim-pc\sql2014')
            self.txtSQLServerUserName.setText('sa')
            self.txtSQLServerPassword.setText('blue123')
            self.txtSQLServerDatabase.setText('orange_market')
            # hide other
            self.lblMySQLPort.hide()
            self.txtMySQLPort.hide()
            self.lblFilePath.hide()
            self.txtImportPath.hide()
            self.btnImport.hide()
            self.lblWebAPIURL.hide()
            self.txtWebAPIURL.hide()
        elif type_import == 3:
            self.lblSQLServerIP.show()
            self.txtSQLServerIP.show()
            self.lblSQLServerUserName.show()
            self.txtSQLServerUserName.show()
            self.lblSQLServerPassword.show()
            self.txtSQLServerPassword.show()
            self.lblMySQLPort.show()
            self.txtMySQLPort.show()
            self.btnSQLServerTest.show()
            self.btnSQLServerSave.show()
            self.lblSQLServerDatabase.show()
            self.txtSQLServerDatabase.show()
            # hide other
            self.lblSQlServerAuth.hide()
            self.cboSQLServerAuth.hide()
            self.lblFilePath.hide()
            self.txtImportPath.hide()
            self.btnImport.hide()
            self.lblWebAPIURL.hide()
            self.txtWebAPIURL.hide()            
        elif type_import == 4:
            self.lblWebAPIURL.show()
            self.txtWebAPIURL.show()
            # hide others
            self.lblSQLServerIP.hide()
            self.txtSQLServerIP.hide()
            self.lblSQLServerUserName.hide()
            self.txtSQLServerUserName.hide()
            self.lblSQLServerPassword.hide()
            self.txtSQLServerPassword.hide()
            self.lblMySQLPort.hide()
            self.txtMySQLPort.hide()
            self.btnSQLServerTest.hide()
            self.btnSQLServerSave.hide()
            self.lblSQlServerAuth.hide()
            self.cboSQLServerAuth.hide()
            self.lblFilePath.hide()
            self.txtImportPath.hide()
            self.btnImport.hide()
            self.lblSQLServerDatabase.hide()
            self.txtSQLServerDatabase.hide()
    @pyqtSlot()
    def on_cbo_sql_server_auth_changed(self):
        idx = self.cboSQLServerAuth.currentIndex()
        if idx == 0 :
            self.lblSQLServerUserName.show()
            self.txtSQLServerUserName.show()
            self.lblSQLServerPassword.show()
            self.txtSQLServerPassword.show()
        else:
            self.lblSQLServerUserName.hide()
            self.txtSQLServerUserName.hide()
            self.lblSQLServerPassword.hide()
            self.txtSQLServerPassword.hide()
    @pyqtSlot()
    def on_server_test_connection_clicked(self):
        try:
            connection_string = ''
            server = self.txtSQLServerIP.text()
            database = self.txtSQLServerDatabase.text()
            auth_type = self.cboSQLServerAuth.currentIndex()
            username = self.txtSQLServerUserName.text()
            password = self.txtSQLServerPassword.text()
            connection = pymssql.connect(server=server, user=None, password=None, database=database)
            if auth_type == 0:
                connection = pymssql.connect(server=server, user=username, password=password, database=database)

            cursor = connection.cursor()
            QMessageBox.information(None, 'Test Connection', "Connect sucessfully!")

            # cursor.execute("select name from sys.tables where type ='U' order by name")
            # self.cboSourceTable.clear()
            # row = cursor.fetchone()
            # while row:
            #     self.cboSourceTable.addItem(row[0])
            #     row = cursor.fetchone()
            
            cursor.close()
            connection.close()
        except Exception as e:
            print(str(e))
            QMessageBox.warning(None,'Test Connection','Connection failed!')
    @pyqtSlot()
    def on_server_save_connection_clicked(self):
        try:
            server = self.txtSQLServerIP.text()
            database = self.txtSQLServerDatabase.text()
            auth_type = self.cboSQLServerAuth.currentIndex()
            username = self.txtSQLServerUserName.text()
            password = self.txtSQLServerPassword.text()
            connection = pymssql.connect(server=server, user=None, password=None, database=database)
            if auth_type == 0:
                connection = pymssql.connect(server=server, user=username, password=password, database=database)

            cursor = connection.cursor()
            cursor.execute("select name from sys.tables where type ='U' order by name")
            self.cboSourceTable.clear()
            row = cursor.fetchone()
            while row:
                self.cboSourceTable.addItem(row[0])
                row = cursor.fetchone()
            
            cursor.close()
            connection.close()
        except Exception as e:
            print(str(e))
            QMessageBox.warning(None,'Loading','Connection Failed!')
    @pyqtSlot()
    def on_cbo_file_type_changed(self):
        try:
            import_type = self.cboFileType.currentIndex()
            self.hideControls(import_type)
        except Exception as e:
            print(str(e))
    @pyqtSlot()
    def browse_import_file_clicked(self):
        fileType = self.cboFileType.currentText()
        # Open File
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseCustomDirectoryIcons
        # if self.fileTypeComboBox
        file, _ = QFileDialog.getOpenFileName(self,"Open File", "",fileType, options=options)
        if file:
            self.txtImportPath.setText(file)
            workbook = open_workbook(file,on_demand=True)
            self.cboSourceTable.clear()
            self.cboSourceTable.addItems(workbook.sheet_names())
    @pyqtSlot()
    def on_cbo_source_table_changed(self):
        source_type = self.cboFileType.currentIndex()
        selected_target = self.cboTargetTable.currentIndex()
        selected_source = self.cboSourceTable.currentText()
        data = self.get_all_source_columns(source_type,selected_source,selected_target)
        if selected_target == 0:
            cursor = self.connection.cursor()
            cursor.execute('select * from item limit 1')
            names = list(map(lambda x: x[0], cursor.description))
            cursor.fetchone()
            self.matchFieldsTableWidget.setRowCount(0)
            row = 0
            for name in names:
                if name != "label":
                    combo = QtWidgets.QComboBox()
                    chkBoxItem = QtWidgets.QTableWidgetItem()
                    chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(QtCore.Qt.Checked)
                    combo.clear()
                    combo.addItems(data)
                    self.matchFieldsTableWidget.insertRow(row)
                    self.matchFieldsTableWidget.setItem(row,0,chkBoxItem)
                    self.matchFieldsTableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(name))
                    self.matchFieldsTableWidget.setCellWidget(row,2,combo)
                    row += 1
            cursor = None
        else:
            print('Sales Transaction')
    @pyqtSlot()
    def on_cbo_target_table_changed(self):
        source_type = self.cboFileType.currentIndex()
        selected_target = self.cboTargetTable.currentIndex()
        selected_source = self.cboSourceTable.currentText()
        data = self.get_all_source_columns(source_type,selected_source,selected_target)
        # print(selected_target)
        if selected_target == 1: # Item Table
            cursor = self.connection.cursor()
            cursor.execute('select * from item limit 1')
            names = list(map(lambda x: x[0], cursor.description))
            cursor.fetchone()
            self.matchFieldsTableWidget.setRowCount(0)
            row = 0
            for name in names:
                if name != "label":
                    combo = QtWidgets.QComboBox()
                    chkBoxItem = QtWidgets.QTableWidgetItem()
                    chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(QtCore.Qt.Checked)
                    combo.clear()
                    combo.addItems(data)
                    self.matchFieldsTableWidget.insertRow(row)
                    self.matchFieldsTableWidget.setItem(row,0,chkBoxItem)
                    self.matchFieldsTableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(name))
                    self.matchFieldsTableWidget.setCellWidget(row,2,combo)
                    row += 1
            cursor = None
        elif selected_target == 2: # Sales Transaction Table
            cursor = self.connection.cursor()
            cursor.execute('select * from sales_transaction limit 1')
            names = list(map(lambda x: x[0], cursor.description))
            cursor.fetchone()
            self.matchFieldsTableWidget.setRowCount(0)
            row = 0
            for name in names:
                if name != "entry_no":
                    combo = QtWidgets.QComboBox()
                    chkBoxItem = QtWidgets.QTableWidgetItem()
                    chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(QtCore.Qt.Checked)
                    combo.clear()
                    combo.addItems(data)
                    self.matchFieldsTableWidget.insertRow(row)
                    self.matchFieldsTableWidget.setItem(row,0,chkBoxItem)
                    self.matchFieldsTableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(name))
                    self.matchFieldsTableWidget.setCellWidget(row,2,combo)
                    row += 1
            cursor = None

    def get_all_source_columns(self,source_type,selected_source,selected_target):
        data = []
        if source_type == 0: # Excel
            path = self.txtImportPath.text()
            workbook = open_workbook(path,on_demand=True)
            sheet = workbook.sheet_by_name(selected_source)
            try:
                sheet_row = sheet.row(0)  # 1st row
                for idx, cell_obj in enumerate(sheet_row):
                    # cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
                    data.append(cell_obj.value)
            except:
                data = []
                print('error')
        elif source_type == 1:
            try:
                sheet_row = sheet.row(0)  # 1st row
                for idx, cell_obj in enumerate(sheet_row):
                    # cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
                    data.append(cell_obj.value)
            except:
                data = []
                print('error')
        elif source_type == 2:
            try:
                server = self.txtSQLServerIP.text()
                database = self.txtSQLServerDatabase.text()
                auth_type = self.cboSQLServerAuth.currentIndex()
                username = self.txtSQLServerUserName.text()
                password = self.txtSQLServerPassword.text()
                sql_server_sonnection = pymssql.connect(server=server, user=None, password=None, database=database,charset='utf8')
                if auth_type == 0:
                    sql_server_sonnection = pymssql.connect(server=server, user=username, password=password, database=database,charset='utf8')
                
                sql_server_cursor = sql_server_sonnection.cursor()
                sql_server_cursor.execute("select c.name as name from sys.columns c inner join sys.tables t on c.object_id = t.object_id where t.name='"+ self.cboSourceTable.currentText() +"' order by c.name")
                row = sql_server_cursor.fetchone()
                data.clear()
                while row:
                    data.append(row[0])
                    row = sql_server_cursor.fetchone()
                sql_server_cursor.close()
                sql_server_sonnection.close()
            except:
                data = []
                print('error')
        # ====================return=============
        return data
    @pyqtSlot()
    def on_do_import_clicked(self):
        source_type = self.cboFileType.currentIndex()
        number_of_rows = self.matchFieldsTableWidget.rowCount()
        target_fields = []
        source_fields = []
        query_source_fields = []
        for row in range(number_of_rows):
            try:
                if self.matchFieldsTableWidget.item(row, 0).checkState() == QtCore.Qt.Checked:
                    target_fields.append(self.matchFieldsTableWidget.item(row, 1).text())
                    widget = self.matchFieldsTableWidget.cellWidget(row, 2)
                    if isinstance(widget, QComboBox):
                        if source_type == 0:
                            source_fields.append(widget.currentIndex())
                        elif source_type == 1:
                            source_fields.append(widget.currentText())
                            # query_source_fields.append('[' + widget.currentText() + ']')
                        elif source_type == 2:
                            source_fields.append(widget.currentText())
                            query_source_fields.append('[' + widget.currentText() + ']')
            except Exception as e:
                print(str(e))
        try:
            if source_type == 0:
                path = self.txtImportPath.text()
                sheetname = self.cboSourceTable.currentText()
                selected_target = self.cboTargetTable.currentIndex()
                if selected_target == 1:
                    result = import_item_from_excel(path,sheetname,source_fields,target_fields,self.connection,False)
                    if result == 'OK':
                        QMessageBox.information(None, 'Import Item', "Import completed!")
                    else:
                        QMessageBox.warning(None, 'Import Item', "Import not completed!")
                elif selected_target == 2:
                    result = import_sales_from_excel(path,sheetname,source_fields,target_fields,self.connection,False)
                    if result == 'OK':
                        QMessageBox.information(None, 'Import Sales', "Import completed!")
                    else:
                        QMessageBox.warning(None, 'Import Sales', "Import not completed!")
            elif source_type == 2:
                
                selected_target = self.cboTargetTable.currentIndex()
                server = self.txtSQLServerIP.text()
                database = self.txtSQLServerDatabase.text()
                auth_type = self.cboSQLServerAuth.currentIndex()
                username = self.txtSQLServerUserName.text()
                password = self.txtSQLServerPassword.text()
                source_table = self.cboSourceTable.currentText()
                if selected_target == 1:
                    result = import_item_from_sqlserver(server,database,auth_type,username,password,source_table,query_source_fields,target_fields,self.connection,False)
                    if result == 'OK':
                        QMessageBox.information(None, 'Import Item', "Import completed!")
                    else:
                        QMessageBox.warning(None, 'Import Item', "Import not completed!")
                elif selected_target == 2:
                    # print(source_fields)
                    # print(query_source_fields)
                    # start_time = datetime.now()
                    result = import_sales_from_sqlserver(server,database,auth_type,username,password,source_table,query_source_fields,target_fields,self.connection,False)
                    # end_time = datetime.now()
                    # insert_activity_log(self.connection,0,)
                    if result == 'OK':
                        QMessageBox.information(None, 'Import Sales', "Import completed!")
                    else:
                        QMessageBox.warning(None, 'Import Sales', "Import not completed!")

        except Exception as error:
            print(str(error))
    