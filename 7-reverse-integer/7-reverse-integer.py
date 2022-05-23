class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        if num[0] == "-":
            num = "-" + num[len(num)-1:0:-1]
        else:
            num = num[::-1]
        num = int(num)
        if num not in range (-(2**31),(2**31)-1):
            return 0
        return num