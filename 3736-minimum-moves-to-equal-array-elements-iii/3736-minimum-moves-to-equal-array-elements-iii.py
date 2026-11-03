class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ele=max(nums)
        res=0
        for i in nums:
            res+=abs(i-ele)
        return res