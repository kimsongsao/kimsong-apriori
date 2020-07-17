import pymssql
from xlrd import open_workbook,cellname, xldate_as_tuple
from xlrd.sheet import ctype_text
import collections

def import_item_from_excel(source_path,source_sheetname,source_columns,target_columns,target_conn,append = False):
    """
    Arguments
        source_path: a path of excel file
        source_sheetname: a sheet name of excel file
        source_columns: a list of source columns
        target_columns: a list of target columns
        target_conn: a connection target database

    Note: source_columns and target_columns must be the same size
    """
    result = None
    if len(source_columns) <= 0:
        return 'no source columns'
    try:
        workbook = open_workbook(source_path,on_demand=True)
        sheet = workbook.sheet_by_name(source_sheetname)
        query = "insert into item (" + ",".join(target_columns) + ",label) VALUES (" + ",".join(["%s"] * len(target_columns))+ ",%s)"                    
        # print(query)
        cursor = target_conn.cursor()
        cursor.execute("delete from item")
        label = 1
        values = []
        for row in range(1, sheet.nrows):                    
            row_values = []
            for col in source_columns:
                row_values.append(sheet.cell_value(row,col))
            # match label
            row_values.append(label)
            values.append(row_values)
            label += 1
        
        cursor.executemany(query, values)
        target_conn.commit()
        cursor.close()
        result = 'OK'
    except Exception as error:
        print(str(error))
        result = None
    return result
def import_item_from_sqlserver(server,database,auth_type,user,password,source_table,source_columns,target_columns,target_conn,append = False):
    """
    Arguments
        server: the SQL Server Address
        database: a name of database
        auth_type: authetication type (Windows/SQL)
        user: a user of login to database
        password: a password of login to database
        source_table: a list of source table name
        source_columns: a list of source columns
        target_columns: a list of target columns
        target_conn: a connection target database
    
    Note: source_columns and target_columns must be the same size
    """
    try:
        connection = pymssql.connect(server=server, user=None, password=None, database=database,charset='utf8')
        if auth_type == 0:
            connection = pymssql.connect(server=server, user=user, password=password, database=database,charset='utf8')
        
        cursor = connection.cursor(as_dict=True)
        sqlserver = "select " + ",".join(source_columns) + " from [" + source_table + "]"
        cursor.execute(sqlserver)
        records = cursor.fetchall()
        values = []
        label = 1
        for row in records:
            row_values = []
            # print(row[source_columns[0]])
            for column in (source_columns):
                column = column.replace("[","")
                column = column.replace("]","")
                row_values.append(row.get(str(column)))
            row_values.append(label)
            values.append(row_values)
            label += 1

        cursor.close()
        connection.close()
        # ====================
        query = "insert into item (" + ",".join(target_columns) + ",label) VALUES (" + ",".join(["%s"] * len(target_columns))+ ",%s)"  
        cur = target_conn.cursor()
        # if not append:
        cur.execute("delete from item")
        cur.executemany(query,values)
        target_conn.commit()
        cur.close()
        return 'OK'
    except Exception as error:
        print(str(error))
        return None
    # ================================
def import_item_from_mysql(host,port,user,password,database,source_table,source_columns,target_columns,target_conn,append = False):
    """
    Arguments
        host: a server host address
        port: access port
        user: a user of login to database
        password: a password of login to database
        source_table: a list of source table name
        source_columns: a list of source columns
        target_columns: a list of target columns
        target_conn: a connection target database
        append: append data
    
    Note: source_columns and target_columns must be the same size
    """
    connection = mariadb.connect(host=host, port=port, user=user, password=password, database=database)
    cursor = connection.cursor(as_dict=True)
    myserver = "select " + ",".join(source_columns) + " from " + source_table
    # print(sql)
    cursor.execute(myserver)
    records = cur.fetchall()
    values = []
    label = 1
    for row in records:
        row_values = []
        # print(row[source_fields[0]])
        for column in source_columns:
            row_values.append(str(row[column]))
        row_values.append(label)
        values.append(row_values)
        label += 1

    cursor.close()
    connection.close()
    # ====================
    query = "insert into item (" + ",".join(target_columns) + ",label) VALUES (" + ",".join(["%s"] * len(target_columns))+ ",%s)"  
    cursor = target_conn.cursor()
    # if not append:
    cursor.execute("delete from item")
    cursor.executemany(query,values)
    target_conn.commit()
    cursor.close()
    # ================================
def import_item_from_oracle():
    print('oracle')
def import_item_from_api():
    print('api')
def import_item_from_csv():
    print('csv')
def fields(cursor):
    """ Given a DB API 2.0 cursor object that has been executed, returns
    a dictionary that maps each field name to a column index; 0 and up. """
    results = {}
    column = 0
    for d in cursor.description:
        results[d[0]] = column
        column = column + 1

    return results