class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res=high-low+1
        if res%2!=0 and low%2!=0:
            return res//2+1
        else:
            return res//2