class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        res=[]
        for i in queries:
            x,y=i[0],i[1]
            ak=[(num[-y:],index) for index,num in enumerate(nums)]
            ak.sort()
            res.append(ak[x-1][1])
        return res