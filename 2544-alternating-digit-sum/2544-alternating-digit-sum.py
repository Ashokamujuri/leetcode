class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n_str=str(n)
        po_sum=sum(int(n_str[i])  for i in range(0,len(n_str),2))
        ne_sum=sum(int(n_str[i])  for i in  range(1,len(n_str),2))
        return po_sum-ne_sum