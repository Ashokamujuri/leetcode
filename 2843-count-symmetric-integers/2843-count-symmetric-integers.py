class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res=0
        for i in range(low,high+1):
            s=str(i)
            if len(s)%2==0:
                hf=len(s)//2
                fi_hf=sum(int(j) for j in s[:hf])
                sec_hf=sum(int(j) for j in s[hf:])

                if fi_hf==sec_hf:
                    res+=1
        return res