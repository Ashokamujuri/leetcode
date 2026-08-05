class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k=[]
        ans=0
        for i in s:
            if i in k:
                k=k[k.index(i)+1:]
            k.append(i)
            ans=max(ans,len(k))
        return ans
