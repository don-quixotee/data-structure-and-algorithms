def Quicksort(a,low, high):
    if low<high:
        pi = partition(a, low, high)
#         print(pi)
        Quicksort(a, low,pi-1)
        Quicksort(a, pi+1, high)

def partition(a, low, high):
    i = low - 1
    pivot = a[high]
    for  j in range(low, high):
        if a[j]<= pivot:
            i = i +1
            a[i] ,a[j] = a[j], a[i]
        
    a[i+1] , a[high] = a[high], a[i+1]
   
    
    
    return i+1


a = [10,12,300,193,2,200,100,3,30,195]
print("usorted a : ",a)
n = len(a)
Quicksort(a, 0, n-1)
print("sorted  a : ",a)
