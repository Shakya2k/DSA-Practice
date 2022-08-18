class Solution(object):
    def binary_search(self,arr):
        l,h,ans = 0,len(arr)-1,-1
        while l<=h:
            mid = (l+h)//2
            x = float("-inf") if mid+1 >= len(arr) else arr[mid+1]
            y = float("-inf") if mid-1 < 0 else arr[mid-1]
            
            if arr[mid]>x and arr[mid]>y:
                ans = mid
                return ans
            
            elif arr[mid]<x:
                l = mid+1
             
            elif arr[mid] < y:
                h = mid-1
            
        return ans
    
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = self.binary_search(nums)
        
        ans = 0 if x==-1 else x
        return ans