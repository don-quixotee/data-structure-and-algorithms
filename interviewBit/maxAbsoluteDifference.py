class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        maxSum = 0 
        currentSum = 0
        for i in range(len(A)):
            for j in range(len(A)):
                currentSum = abs(A[i] - A[j]) + abs(i - j)
                if maxSum < currentSum:
                    maxSum = currentSum
        return maxSum

