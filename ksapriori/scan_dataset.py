def scan_dataset(data, candidates, min_support):
    """
    Scan through transaction data and return a list of candidates that meet
    the minimum support threshold, and support data about the current candidates.
    Arguments:
        data: data set,
        candidates: a list of candidate sets
        min_support: the minimum support
    """
    count = {}
    for tid in data:
        for candidate in candidates:
            if candidate.issubset(tid):
                if not candidate in count: count[candidate] = 1
                else: count[candidate] += 1
    num_of_trans = float(len(data))
    candidate_list = []
    support_data = {}
    # calculate support for every itemset
    for key in count:
        support_count = count[key]
        # support_count = count[key]
        # support = count[key] / num_of_trans # in percentage
        support = (count[key] / num_of_trans) * 100 # in percentage
        # print(count[key]) 
        # If the support meets the minimum support requirements, 
        # add it to the list of itemsets.
        if support >= min_support:
            candidate_list.insert(0,key)
        support_data[key] = support
    return candidate_list, support_data