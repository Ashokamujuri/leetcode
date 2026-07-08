class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)  
        voe = 'aeiouAEIOU'
        i, j = 0, n - 1
        while i < j:
            if s[i] not in voe:
                i += 1
            elif s[j] not in voe:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
                
        return "".join(s) 