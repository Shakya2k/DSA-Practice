class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        product = 1
        
        while product <= n:
            if product == n:
                return True
            product *= 4
        return False
        