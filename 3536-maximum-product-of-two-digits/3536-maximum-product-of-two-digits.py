class Solution:
    def maxProduct(self, n: int) -> int:
        if n<=9:
            return n
        digit=[int(i) for i in str(n)]
        digit.sort(reverse=True)
        return digit[0]*digit[1]