class Solution:
    def isFascinating(self, n: int) -> bool:
        res=str(n)+str(n*2)+str(n*3)
        return "".join(sorted(res))=='123456789'