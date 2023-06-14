def cxSet(ind1, ind2):
    temp = ind1
    ind1 &= ind2
    ind2 ^= temp
    return ind1, ind2