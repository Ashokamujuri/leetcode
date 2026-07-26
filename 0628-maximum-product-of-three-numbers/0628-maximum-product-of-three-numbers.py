class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a=nums[-1]*nums[-2]*nums[-3]
        k=nums[1]*nums[-1]*nums[0]
        return max(a,k)
