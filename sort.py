def avgsorted(num_list):
    rslt = []
    for avg in range(len(num_list)):
        if avg > sum(num_list) / len(num_list):
            rslt.append(avg)
    return rslt

avgsorted([1, 2, 3, 4, 5, 6, 7])