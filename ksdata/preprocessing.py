from datetime import datetime
def generate_preprocessing(connection,from_date,to_date):
    cursor = connection.cursor()
    sql = 'delete from preprocessing_transaction'
    cursor.execute(sql)
    sql = "SELECT d.document_no, "
    sql = sql + " GROUP_CONCAT(DISTINCT i.label SEPARATOR ',') "
    sql = sql + " as item FROM  sales_transaction as d "
    sql = sql + " INNER JOIN item i on d.item_no = i.no "
    sql = sql + " WHERE posting_date BETWEEN '" + str(from_date)
    sql = sql + "' and '"+ str(to_date) +"' GROUP BY d.document_no "
    insert_query = "insert into preprocessing_transaction"
    insert_query = insert_query + "(document_no,item) " + sql
    cursor.execute(insert_query)
    return cursor.rowcount


