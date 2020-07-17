from datetime import datetime
def get_rules_list(connection,antecedent_filter,consequent_filter):
    """
    Arguments:
        connection: a connection to database
        antecedent_filter: filtering
        consequent_filter: filtering
    """
    # select to list
    select_cursor = connection.cursor()
    select_query = "select antecedent,consequent,support,confidence from association_rules where 1=1"
    if len(antecedent_filter) > 0:
        antecedent_filter = antecedent_filter.replace("'","''")
        select_query = select_query + " and antecedent like '%" + antecedent_filter + "%'"
    if len(consequent_filter) > 0:
        consequent_filter = consequent_filter.replace("'","''")
        select_query = select_query + " and consequent like '%" + consequent_filter + "%'"
    select_cursor.execute(select_query)
    records = select_cursor.fetchall()
    select_cursor.close()
    return records
def insert_rule(connection,rules):
    rule_cursor = connection.cursor()
    rule_cursor.execute("delete from association_rules")
    rule_insert = "insert into association_rules(antecedent_key,antecedent,consequent_key,consequent,support,confidence,created_at) values(%s,%s,%s,%s,%s,%s,%s)"
    rule_insert_value = []
    for row in rules:
        created_at = datetime.now()
        antecedent_key = str(row[0])
        antecedent = antecedent_key.replace("frozenset(","")
        antecedent = antecedent.replace(")","")
        consequent_key = str(row[1])
        consequent = consequent_key.replace("frozenset(","")
        consequent = consequent.replace(")","")
        row = (antecedent_key,antecedent,consequent_key,consequent,float(row[2]),int(row[3] * 100),str(created_at))
        rule_insert_value.append(row)
    rule_cursor.executemany(rule_insert,rule_insert_value)
    rule_cursor.close()
