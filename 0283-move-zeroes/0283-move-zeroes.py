class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        temp=[0]*n
        k=0
        for i in nums:
            if i!=0:
                temp[k]=i
                k+=1
        for i in range(n):
            nums[i]=temp[i]
        return nums