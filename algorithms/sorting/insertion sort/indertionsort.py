

def insertionSort(alist):

    for i in range(1, len(alist)):
        value = alist[i]
        j = i-1

        while (j >= 0 and value < alist[j]):
            alist[j+1] = alist[j]
            j = j - 1

        alist[j+1] = value
    return alist




num = [25,17,31,13,2]
print(insertionSort(num))
