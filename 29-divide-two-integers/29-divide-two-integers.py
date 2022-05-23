class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        result = 0
        remain = abs(dividend)
        pdivisor = abs(divisor)
        while remain >= pdivisor:
            mult = pdivisor
            times = 1
            while mult <= remain:
                mult *= 2
                times *= 2
            mult //= 2
            times //= 2
            remain -= mult
            result += times
        
        if ((dividend > 0 and divisor > 0) or 
            (dividend < 0 and divisor < 0)):
            return result
        return -result