class Solution:
    def myAtoi(self, s: str) -> int:
        sign=1
        s=s.strip()
        if s=="":
            return 0
        if s[0]=='-':
            sign=-1
        num=0
        for x,y in enumerate(s):
            if (y=='+' or y=='-') and x==0:
                pass
            elif y.isdigit():
                num=10*num+int(y)
            else:
                break
        num=num*sign
        
        if num < -2**31:
            num = -2**31
        elif num >= 2**31:
            num = 2**31-1
        return num