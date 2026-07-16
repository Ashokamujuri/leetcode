class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a,b):
            while b!=0:
                r=a%b
                a=b
                b=r
            return a
        prefixGcd=[]
        mxi=0
        ak=nums[:]
        n=len(ak)
        
        for i in range(n):
            mxi=max(mxi,ak[i])
            prefixGcd.append(gcd(ak[i],mxi))
        prefixGcd.sort()
        res,le,ri=0,0,n-1
        while le<ri:
            res+=gcd(prefixGcd[le],prefixGcd[ri])
            le+=1
            ri-=1
        return res