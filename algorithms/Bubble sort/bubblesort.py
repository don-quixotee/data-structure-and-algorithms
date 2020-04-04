
"""
Bubble Sort
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent 
elements if they are in wrong order.

"""

def BubbleSort1 (num):
    n = len(num)

    for i in range(n):
        for j in range(0, n-i-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

    return num
    """
    time complexity for this sort is  O(n^2) time 
    which can be optimized more    
    """
def BubbleSort2(num):
    n = len(num)
    
    for i in range(n):
        swapped = False
        for j in range(i+1, n-i-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                swapped = True


        if swapped == False:
            break
    return num






n = [1,6,7,7,6,54,5,43,7,4,4,6]
print(BubbleSort1(n))
print(BubbleSort2(n))