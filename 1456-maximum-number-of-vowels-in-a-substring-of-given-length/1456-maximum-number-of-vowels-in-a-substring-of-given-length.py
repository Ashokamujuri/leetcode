class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow="aeiou"
        vow_co=0
        for i in range(k):
            if s[i] in vow:
                vow_co+=1
        res=vow_co
        for i in range(k,len(s)):
            if s[i] in vow:
                vow_co+=1
            if s[i-k] in vow:
                vow_co-=1
            if vow_co>res:
                res=vow_co
        return res
