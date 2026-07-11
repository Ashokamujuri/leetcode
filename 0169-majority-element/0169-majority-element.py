class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s={}
        n=len(nums)
        for i in nums:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
            if s[i]>n//2:
                return i


