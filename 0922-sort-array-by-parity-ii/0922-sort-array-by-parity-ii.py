class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        odd=[]
        even=[]
        for num in nums:
            if num%2==0:
                even.append(num)
            else:
                odd.append(num)
        res=[]
        for e,o in zip(even,odd):
            res.append(e)
            res.append(o)
        return res