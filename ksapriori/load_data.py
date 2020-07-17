def load_dataset(connection):
    select_cursor = connection.cursor()
    select_query = "select item from preprocessing_transaction"
    select_cursor.execute(select_query)
    dataset = []
    for data in select_cursor.fetchall():
        item = list(data[0].split(","))
        dataset.append(item)
    select_cursor.close()   
    # total_tran = len(dataset)
    return dataset