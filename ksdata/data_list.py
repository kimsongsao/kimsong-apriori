def get_item_list(connection,code,label,desc,desc2,uom,unit_price):
    records = []
    sql = "select no,label,description,description_2,base_unit_of_measure,unit_price from item where 1=1"
    if len(str(code)) > 0:
        sql = sql + " and no like '%" + code + "%'"
    if len(str(label)) > 0:
        sql = sql + " and label like '%" + label + "%'"
    if len(str(desc)) > 0:
        sql = sql + " and description like '%" + desc + "%'"
    if len(str(desc2)) > 0:
        sql = sql + " and description_2 like '%" + desc2 + "%'"
    if len(str(uom)) > 0:
        sql = sql + " and base_unit_of_measure like '%" + uom + "%'"
    if len(str(unit_price)) > 0:
        sql = sql + " and unit_price =" + unit_price
    cur = connection.cursor()
    cur.execute(sql)
    records = cur.fetchall()
    cur.close()
    return records
def get_sales_transaction_list(connection):
    records = []
    sql = "select * from sales_transaction where 1=1"
    if len(str(code)) > 0:
        sql = sql + " and code like '%" + code + "%'"
    if len(str(label)) > 0:
        sql = sql + " and label like '%" + label + "%'"
    if len(str(desc)) > 0:
        sql = sql + " and description like '%" + desc + "%'"
    if len(str(desc2)) > 0:
        sql = sql + " and description_2 like '%" + desc2 + "%'"
    if len(str(uom)) > 0:
        sql = sql + " and unit_of_measure like '%" + uom + "%'"
    if len(str(unit_price)) > 0:
        sql = sql + " and unit_price =" + unit_price
    cur = connection.cursor()
    cur.execute(sql)
    records = cur.fetchall()
    cur.close()
    return records
