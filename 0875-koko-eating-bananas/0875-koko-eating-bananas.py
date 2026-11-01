class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low,high=1,max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            hrs=0
            for i in piles:
                hrs+=math.ceil(i/mid)
            if hrs<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

