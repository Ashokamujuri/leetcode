class Solution:
    def sumAndMultiply(self, n: int) -> int:
        arr=[i for i in str(n) if i!='0']
        if not arr:
            return 0
        x=int("".join(arr))
        digit_sum=sum(int(i) for i in arr)
        return x*digit_sum        