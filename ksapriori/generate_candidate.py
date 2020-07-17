def create_c1(dataset):
    """
    Create a list of unique items in transaction data.
    Represent each item as a set of length 1.
    """
    c = []
    for data in dataset:
        for item in data:
            if not [item] in c:
                c.append([item])
    c.sort()
    return list(map(frozenset, c))
def create_ck(frequent_itemset, k):
    """
    Create a list of candidates of length k.
    Arguments:
        frequent_itemset: a list of frequent itemsets
        k: the size of the itemsets
    
    """
    candidate_list = []
    len_freq_itemsets = len(frequent_itemset)
    for i in range(len_freq_itemsets):
        for j in range(i + 1, len_freq_itemsets):
            L1 = list(frequent_itemset[i])[:k-2]  # [0,1] | [0,2] -> [0,1,2]
            L2 = list(frequent_itemset[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                candidate_list.append(frequent_itemset[i] | frequent_itemset[j])
    return candidate_list