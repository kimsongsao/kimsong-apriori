import mysql.connector as mariadb

def create_open_database(host,port,user,password,db_name = 'ksapriori'):
    conn = None
    try:
        connection = mariadb.connect(host=host,port=port,user=user,password=password)
        cursor = connection.cursor()
        cursor.execute("select * from information_schema.schemata where schema_name = '" + db_name +"'")
        db = cursor.fetchone()
        if db == None:
            create_db = create_database(connection,db_name,cursor)
            if create_db:
                print(123)
                conn = mariadb.connect(host=host,port=port,user=user,password=password,database=db_name,connection_timeout=36000)
                cur = conn.cursor()
                create_table(conn,db_name,cur)
                cur.close()
                conn.close()
            cursor.close()
            connection.close()
            conn = mariadb.connect(host=host,port=port,user=user,password=password,database=db_name,connection_timeout=36000)
        else:
            conn = mariadb.connect(host=host,port=port,user=user,password=password,database=db_name,connection_timeout=36000)
    except Exception as error:
        conn = None
    return conn
def create_database(connection,db,cursor):
    result = False
    try:
        db_sql = "create database if not EXISTS "+ db +" character set utf8 collate utf8_general_ci"
        cursor.execute(db_sql)
        result = True
    except Exception as error:
        print(str(error))
        result = True
    return result
def create_table(connection,db,cursor):
    try:
        # apriori_filter
        table = "CREATE TABLE IF NOT EXISTS `apriori_filter` ("
        table += "`id` int(11) NOT NULL AUTO_INCREMENT,"
        table += "`from_date` date DEFAULT NULL,"
        table += "`to_date` date DEFAULT NULL,"
        table += "`min_support` decimal(32,18) DEFAULT 0.000000000000000000,"
        table += "`min_confidence` decimal(32,18) DEFAULT 0.000000000000000000,"
        table += "`num_of_transaction`  int(11) NULL DEFAULT 0 ,"
        table += "`created_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),"
        table += " PRIMARY KEY (`id`)"
        table += " ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;"
        cursor.execute(table)
        # activity_log
        table = "CREATE TABLE IF NOT EXISTS `activity_log` ("
        table += "`id` int(11) NOT NULL AUTO_INCREMENT,"
        table += "`apriori_filter_id` int(11) NOT NULL,"
        table += "`name` varchar(255) DEFAULT NULL,"
        table += "`start_time` timestamp NULL,"
        table += "`end_time` timestamp NULL,"
        table += " PRIMARY KEY (`id`)"
        table += " ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        cursor.execute(table)
        # association_rules
        table = "CREATE TABLE IF NOT EXISTS `association_rules` ("
        table += "`id` int(11) NOT NULL AUTO_INCREMENT,"
        table += "`from_date` datetime DEFAULT NULL,"
        table += "`to_date` datetime DEFAULT NULL,"
        table += "`antecedent_key` varchar(250) DEFAULT '',"
        table += "`antecedent` varchar(250) DEFAULT NULL,"
        table += "`consequent_key` varchar(250) DEFAULT '',"
        table += "`consequent` varchar(250) DEFAULT NULL,"
        table += "`lift` decimal(32,18) DEFAULT NULL,"
        table += "`support` decimal(32,18) DEFAULT NULL,"
        table += "`confidence` decimal(32,18) DEFAULT NULL,"
        table += "`created_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),"
        table += "`updated_at` timestamp NULL DEFAULT NULL,"
        table += "PRIMARY KEY (`id`)"
        table += ") ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;"
        cursor.execute(table)
        
        # frequent itemset
        table = "CREATE TABLE IF NOT EXISTS `frequent_itemset` ("
        table += "`id` int(11) NOT NULL AUTO_INCREMENT,"
        table += "`support_key` varchar(255) DEFAULT NULL,"
        table += "`support_data` text DEFAULT NULL,"
        table += "`itemset` varchar(250) DEFAULT NULL,"
        table += "`total_transaction` int(11) DEFAULT NULL,"
        table += "`support_count` int(11) DEFAULT NULL,"
        table += "`support_percentage` decimal(32,18) DEFAULT 0.000000000000000000,"
        table += "`created_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),"
        table += "`updated_at` timestamp NULL DEFAULT NULL,"
        # table += "`from_date_filter` date DEFAULT NULL,"
        # table += "`to_date_filter` date DEFAULT NULL,"
        # table += "`min_support_filter` decimal(32,18) DEFAULT NULL,"
        # table += "`max_itemset_filter` int(11) DEFAULT NULL,"
        table += " PRIMARY KEY (`id`)"
        table += " ) ENGINE=InnoDB AUTO_INCREMENT=63219 DEFAULT CHARSET=utf8;"
        cursor.execute(table)
        # Item
        table = "CREATE TABLE IF NOT EXISTS `item` ("
        table += "`no` varchar(100) NOT NULL,"
        table += "`no_2` varchar(100) DEFAULT NULL,"
        table += "`label` int(11) DEFAULT 0,"
        table += "`description` varchar(255) DEFAULT NULL,"
        table += "`description_2` varchar(255) DEFAULT NULL,"
        table += "`base_unit_of_measure` varchar(50) DEFAULT NULL,"
        table += "`unit_price` decimal(32,18) DEFAULT 0.000000000000000000,"
        table += " PRIMARY KEY (`no`)"
        table += " ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        cursor.execute(table)
        # preprocessing_transaction
        table = "CREATE TABLE IF NOT EXISTS `preprocessing_transaction` ("
        table += "`document_no` varchar(50) NOT NULL,"
        table += "`item` text DEFAULT NULL,"
        table += " PRIMARY KEY (`document_no`)"
        table += " ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        cursor.execute(table)
        # sales transaction
        table = "CREATE TABLE IF NOT EXISTS `sales_transaction` ("
        table += "`entry_no` int(11) NOT NULL AUTO_INCREMENT,"
        table += "`document_type` varchar(50) DEFAULT 'Invoice',"
        table += "`document_no` varchar(100) DEFAULT NULL,"
        table += "`posting_date` date DEFAULT NULL,"
        table += "`customer_no` varchar(50) DEFAULT NULL,"
        table += "`customer_name` varchar(255) DEFAULT NULL,"
        table += "`currency_code` varchar(50) DEFAULT NULL,"
        table += "`item_no` varchar(100) DEFAULT NULL,"
        table += "`unit_of_measure_code` varchar(100) DEFAULT 'UNIT',"
        table += "`quantity` decimal(32,18) DEFAULT 0.000000000000000000,"
        table += "`unit_price` decimal(32,18) DEFAULT 0.000000000000000000,"
        table += "`amount` decimal(32,18) DEFAULT 0.000000000000000000,"
        table += " PRIMARY KEY (`entry_no`),"
        table += " KEY `idx1` (`document_no`,`posting_date`)"
        table += " ) ENGINE=InnoDB AUTO_INCREMENT=2812307 DEFAULT CHARSET=utf8;"
        cursor.execute(table)
        result = True
    except Exception as error:
        print(str(error))
        result = False
    return result