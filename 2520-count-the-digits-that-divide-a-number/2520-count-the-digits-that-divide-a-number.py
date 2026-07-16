class Solution:
    def countDigits(self, num: int) -> int:
        res=0
        n_str=str(num)
        def check(num,k):
            return num%k==0
        for i in n_str:
            if check(num,int(i)):
                res+=1
        return res
