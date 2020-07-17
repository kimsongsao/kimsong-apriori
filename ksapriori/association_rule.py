from ksapriori.generate_candidate import create_c1,create_ck
def calculate_confidence(freqent_itemset,next_itemset,support_data,min_confidence,rule_list):
    """
    Arguments:
        frequent_itemsets: a list of frequent_itemset
        next_itemset : a list of next iteration
        support_data: a list of itemsets support data
        min_confidence: a minimum confidence threshold in percentage
        rule_list : a list of association rules

        Return as Pruned List
    """
    pruned_list = []
    for consequent in next_itemset:
        confidence = support_data[freqent_itemset] / support_data[freqent_itemset - consequent]
        print(confidence)
        if confidence >= min_confidence:
            print (set(freqent_itemset - consequent), '-->', set(consequent), 'conf:', confidence * 100, '%')
            rule_list.append((freqent_itemset - consequent, consequent, support_data[freqent_itemset], confidence))
            pruned_list.append(consequent)
    return pruned_list

def rules_from_consequent(freqent_itemset,next_itemset,support_data,min_confidence,rule_list):
    """
    Arguments:
        frequent_itemsets: a list of frequent_itemset
        next_itemset : a list of next iteration
        support_data: a list of itemsets support data
        rule_list : a list of association rules

        Return as Pruned List
    """
    tmp1 = []
    m = len(next_itemset[0])
    if (len(freqent_itemset) > (m + 1)):
        tmp1 = create_ck(next_itemset, m + 1) # Gen list of next iteration
        tmp1 = calculate_confidence(freqent_itemset, tmp1, support_data,min_confidence, rule_list) # pruning. pick qualified rules.
    if (len(tmp1) > 1):
        calculate_confidence(freqent_itemset, tmp1, support_data,min_confidence, rule_list) # Continue\Iterate to next level
    
def generate_rule(frequent_itemsets,support_data,min_confidence):
    rule_list = []
    min_confidence = min_confidence / 100
    try:
        for i in range(1, len(frequent_itemsets)):
            for freq_itemset in frequent_itemsets[i]:
                # {0,1,2} -> [{0},{1},{2}].
                next_itemset = [frozenset([item]) for item in freq_itemset]
                if (i > 1): # length > 2, go level by level
                    rules_from_consequent(freq_itemset,next_itemset,support_data,min_confidence,rule_list)
                else: # if only 2 items, just prune - the base
                    calculate_confidence(freq_itemset,next_itemset,support_data,min_confidence,rule_list)
    except Exception as error:
        print("Rule : " + str(error))
        
    return rule_list
