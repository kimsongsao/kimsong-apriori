def get_last_apriori_filter(connection):
     # select to list
    select_cursor = connection.cursor()
    select_query = "select from_date,to_date,min_support,min_confidence from apriori_filter order by id desc limit 1"
    select_cursor.execute(select_query)
    record = select_cursor.fetchone()
    select_cursor.close()
    return record
def insert_apriori_filter(connection,from_date,to_date,min_support,min_confidence,num_of_transaction):
     """
     """
     sql = "insert into apriori_filter(from_date,to_date,min_support,min_confidence,num_of_transaction) values(%s,%s,%s,%s,%s)"
     # created_at = 
     value = (from_date,to_date,min_support,min_confidence,num_of_transaction)
     cur = connection.cursor()
     cur.execute(sql,value)
     return cur.lastrowid
