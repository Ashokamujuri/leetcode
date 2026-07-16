class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            if x>0:
                return 1
            if x<0:
                return -1
            if x==0:
                return 0
        pro=1
        for i in nums:
            pro=pro*i
        return signFunc(pro)