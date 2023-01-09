def kadaneAlgorithm(array):
    l = 0
    r = 0
    maxEndingHere = array[0]
    maxSoFar = array[0]
    s = 0
 
    for i in range(1, len(array)):
        r = i
        print(l,r)
        maxEndingHere += array[i]
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
        if maxEndingHere < 0:
            maxEndingHere = 0
            if(i + 1 < len(array)):
                l = i+1
    return maxSoFar
