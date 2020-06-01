
def selectionSort(a):
    n = len(a)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if a[j]<a[min]:
                min = j
                
        if min != i:
            a[i],a[min] = a[min], a[i]
            

a = [7,4,10,8,3,1]
selectionSort(a)
print(a)


