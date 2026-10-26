class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans=float("inf")
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1

            while j<k:
                summ=nums[i]+nums[j]+nums[k]
                if summ==target:
                    return summ
                if abs(target-summ)<abs(target-ans):
                    ans=summ
                if summ<target:
                    j+=1
                else:
                    k-=1
        return ans