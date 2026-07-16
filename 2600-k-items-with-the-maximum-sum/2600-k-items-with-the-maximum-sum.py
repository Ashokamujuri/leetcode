class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        while k > 0 and numOnes > 0:
            res += 1
            k -= 1
            numOnes -= 1
            
        while k > 0 and numZeros > 0:
            res += 0  # Doesn't change the sum, just consumes k
            k -= 1
            numZeros -= 1
            
        while k > 0 and numNegOnes > 0:
            res -= 1
            k -= 1
            numNegOnes -= 1
            
        return res