class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        N = len(A)
        sumN = sum(A)
        sumSetN = sum(set(A))
        sumNnum = (N*(N + 1))//2
        repeatN = sumN - sumSetN
        missingN = repeatN + (sumNnum - sumN)
        return(repeatN, missingN)
