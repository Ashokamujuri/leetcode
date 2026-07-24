class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp_hi=[i for i in heights]
        exp_hi.sort()
        res=0
        for i in range(len(heights)):
            if exp_hi[i]!=heights[i]:
                res+=1
        return res