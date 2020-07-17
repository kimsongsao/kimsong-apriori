def get_itemset_list(connection,chk,min_support,contain):
    """
    Arguments:
        connection: a connection to database
        chk: - If True, show only itemset that has support greater than minimum support
             - Else, show all itemsets
        min_support: minimum support
        contain: filtering
    """
    select_cursor = connection.cursor()
    select_query = "select itemset,total_transaction,support_count,support_percentage,support_key from frequent_itemset where 1=1"
    if(chk) and (len(min_support) > 0):
        select_query = select_query + " and support_percentage >= " + min_support
    if len(contain) > 0:
        contain = contain.replace("'","''")
        select_query = select_query + " and itemset like '%" + contain + "%'"

    # print(select_query)
    select_cursor.execute(select_query)
    records = select_cursor.fetchall()
    select_cursor.close()
    return records
def insert_itemset(connection,support_data,total_tran):
    itemset_insert = "insert into frequent_itemset(itemset,support_key,support_count,support_percentage,total_transaction) values(%s,%s,%s,%s,%s)"
    itemset_insert_value = []
    itemset_cursor = connection.cursor()
    itemset_cursor.execute("delete from frequent_itemset")
    for key in support_data.keys():
        itemset = str((key))
        itemset = itemset.replace("frozenset(","")
        itemset = itemset.replace(")","")
        row = (itemset,str(key),int(support_data[key] * total_tran / 100),support_data[key],total_tran)
        itemset_insert_value.append(row)
    itemset_cursor.executemany(itemset_insert,itemset_insert_value)
    itemset_cursor.close()