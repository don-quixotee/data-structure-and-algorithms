class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_so_far = 0
        current_max = 0
        
        for i in range(0,len(A)):
            current_max += A[i]
            if current_max < 0:
                current_max = 0
            elif max_so_far < current_max:
                max_so_far = current_max
            
        return max_so_far
        
     
