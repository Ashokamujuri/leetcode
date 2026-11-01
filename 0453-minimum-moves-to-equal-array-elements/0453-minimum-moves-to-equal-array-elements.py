class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_ele=min(nums)
        return sum(i-min_ele for i in nums)