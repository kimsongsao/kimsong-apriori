def insert_activity_log(connection,filter_id,name,start_time,end_time):
    """
    """
    sql = "insert into activity_log(apriori_filter_id,name,start_time,end_time) values(%s,%s,%s,%s)"
    value = (filter_id,name,start_time,end_time)
    cur = connection.cursor()
    cur.execute(sql,value)
