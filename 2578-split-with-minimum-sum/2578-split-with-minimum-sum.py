class Solution:
    def splitNum(self, num: int) -> int:
        digs=[i for i in str(num)]
        digs.sort()
        num1=""
        num2=""
        for i in range(0,len(digs),2):
            num1=num1+digs[i]
        for i in range(1,len(digs),2):
            num2=num2+digs[i]
        return int(num1)+int(num2)
