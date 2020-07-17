from ksapriori.generate_candidate import create_c1,create_ck
from ksapriori.scan_dataset import scan_dataset

def ksapriori(dataset,min_support):
    # start from size 1
    c1 = list(create_c1(dataset))
    data = list(map(set, dataset))
    f1, support_data = scan_dataset(data, c1, min_support)
    #=================================
    freq_itemsets = [f1]
    k = 2
    print ('Level : ', len(freq_itemsets[0]))
    while(len(freq_itemsets[k-2]) > 0):
        print ('Level : ', len(freq_itemsets[k-2]))
        ck =   create_ck(freq_itemsets[k-2], k)
        fk, support_data_k = scan_dataset(data, ck, min_support)
        support_data.update(support_data_k)
        freq_itemsets.append(fk)
        k += 1
    return freq_itemsets, support_data
