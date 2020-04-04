

def selectionSort(num):
    for i in range(len(num)):
        min_idx = i
        for j in range(i+1, len(num)):
            if num[min_idx] > num[j]:
                min_idx = j

        num[i],num[min_idx] = num[min_idx], num[i]
    return num




n = [2,4,1,3,6,7,5,6,9]
print(selectionSort(n))


"""
Time Complexity: O(n2) as there are two nested loops.

Auxiliary Space: O(1)
The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.
"""
