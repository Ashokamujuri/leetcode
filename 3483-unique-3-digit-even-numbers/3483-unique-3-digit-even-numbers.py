class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from collections import Counter


        frq = Counter(digits)
        ans = []
        for num in range(100, 1000, 2):  # Upper bound changed to 1000
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            req = Counter([d1, d2, d3])
            if all(frq[d] >= count for d, count in req.items()):
                ans.append(num)
        return len(ans)