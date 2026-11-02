class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def funn(arr,mid):
            st_cnt=1
            pages=0
            for page in arr:
                if pages+page<=mid:
                    pages+=page
                else:
                    st_cnt+=1
                    pages=page
            return st_cnt
        n=len(nums)
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            if(funn(nums,mid)<=k):
                high=mid-1
            else:
                low=mid+1
        return low