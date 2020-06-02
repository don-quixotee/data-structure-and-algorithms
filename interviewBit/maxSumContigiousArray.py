class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_start, max_stop = 0, 1 # Start, Stop of maximum sub-array
        curr = 0                   # pointer to current array
        max_sum = A[0]         # Sum of maximum array
        current_sum = 0            # sum of current array
    
        for i, elem in enumerate(A):
            current_sum +=  elem
    
            if max_sum < current_sum:
                max_sum = current_sum 
            if current_sum < 0:
                current_sum = 0

        return  max_sum
             
