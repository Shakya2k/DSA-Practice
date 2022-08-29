# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 1
        right = n
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if n==1 or (isBadVersion(mid) == True and isBadVersion(mid-1) == False):
                return mid
            
            elif isBadVersion(mid) == True:
                right = mid - 1
                
            elif isBadVersion(mid) == False:
                left = mid + 1
        
        return -1