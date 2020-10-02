def shellSort(inpList):
    
    gap = len(inpList) // 2

    while gap > 0:

        for i in range(gap, len(inpList)):
            temp = inpList[i]
            j = i

            while j >= gap and inpList[j - gap] > temp:
                inpList[j] = inpList[j - gap]
                j = j-gap
            inpList[j] = temp

        gap = gap//2


