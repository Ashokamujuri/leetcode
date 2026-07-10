class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[]
        for i in range(n+1):
            k=bin(i)
            arr.append(k.count('1'))
        return arr
        