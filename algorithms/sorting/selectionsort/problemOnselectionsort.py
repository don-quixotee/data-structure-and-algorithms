
"""
The task is to complete select() function which is used to implement Selection Sort.

Input:
First line of the input denotes number of test cases 'T'. First line of the test case is the size of array and second line consists of array elements.


Output:
Sorted array in increasing order is displayed to the user.


Constraints:
1 <=T<= 50
1 <=N<= 1000
1 <=arr[i]<= 1000


Example:

Input:
2
5
4 1 3 9 7
10
10 9 8 7 6 5 4 3 2 1

Output:
1 3 4 7 9
1 2 3 4 5 6 7 8 9 10
"""








#User function Template for python3

def select(arr):
    
    # add code here
    
    for i in range(len(arr)):
        min_idx = i
        
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        arr[i] , arr[min_idx] = arr[min_idx] , arr[i]
    
    return arr



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        select(arr)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends