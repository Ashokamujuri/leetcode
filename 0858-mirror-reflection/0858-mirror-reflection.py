class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        import math
        g=math.gcd(p,q)
        p//=g
        q//=g
        def isodd(n):
            return n%2!=0
        if not isodd(p) and isodd(q):
            return 2
        if isodd(p) and isodd(q):
            return 1
        if isodd(p) and not isodd(q):
            return 0
