class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        dig='123456789'
        res=[]
        min_len=len(str(low))
        max_len=len(str(high))
        for l in range(min_len,max_len+1):
            for st in range(10-l):
                num=int(dig[st:st+l])
                if low<=num<=high:
                    res.append(num)
        return res
