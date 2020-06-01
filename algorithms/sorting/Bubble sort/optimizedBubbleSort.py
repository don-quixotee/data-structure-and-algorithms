def bubbleSort(a, n):
    
    for i in range(0,n):
        flag = 0
        for j in range(0, n-1-i):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = 1
                
        if flag == 0:
            break
a = [7,4,10,8,3,1]
bubbleSort(a, len(a))
print(a)
                
