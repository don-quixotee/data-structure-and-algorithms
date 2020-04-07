def insertionsort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        pos = i

        while pos > 0 and alist[pos-1] > key:
            alist[pos] = alist[pos -1]
            pos = pos - 1

        alist[pos] = key
alist = [3,6,8,435,3,5,6,6,43,1]
insertionsort(alist)
print(alist)