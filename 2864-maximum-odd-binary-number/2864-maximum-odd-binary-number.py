class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        o_c=s.count('1')
        z_c=s.count('0')
        return "1"*(o_c-1) + '0'*z_c +'1'

        