def returnNum(n, k):
    returnDict = {}
    for i in range(2**n):
        returnDict[i] = getNumOne(i)
    sortedValues = sorted(returnDict.values())
    value = sortedValues[k]
    newDict = {}; actualDict = {}
    for i, j in returnDict.iteritems():
        if j < value:
            newDict[i] = j
        if j >= value:
            actualDict[i] = j
    num = k - len(newDict)
    decVal = sorted(actualDict.keys())[num-1]
    print bin(decVal)
    
def getNumOne(k):
    oneBits = 0
    while k != 0:
        if k % 2 == 1:
            oneBits += 1
        k = k >> 1
    return oneBits
