class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        product = 1
        while product <= n:
            if product == n:
                return True
            product *= 3
        return False
        