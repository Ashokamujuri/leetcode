class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        md=nums[len(nums)//2]
        return sum(abs(num-md) for num in nums)