def merge(a, lb, mid, ub):
    
    i = ub
    j = mid + 1
    k = lb
    
    while ( i < mid  and j <= ub ):
        if(a[i] <= a[j] ):
            b[k] =a[j]
            i = i + 1
            k = k + 1
        else:
            b[k] = a [j]
            j = j + 1
            k = k + 1
            
    if (i > mid):
        while j <= ub:
            b[k] = a[j]
            j = j + 1
            k = k + 1
    else:
        while i <= mid :
            b [k] = a [i]
            i = i + 1
            k = k + 1
            
            
def mergeSort(a, lb, up):
    if lb<ub:
        mid = (lb + ub )//2
        mergeSort(a, lb, mid )
        mergeSort(a, mid+1, ub)
        merge(a, lb, mid, ub )
        
    
        
        
    
a = [20,10,200,100,300,900,2,6,7,1]
lb = 0
ub = len(a) - 1
mergeSort(a, lb,ub)
print(a)