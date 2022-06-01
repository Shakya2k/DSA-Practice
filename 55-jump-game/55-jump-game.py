class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_vis = 0
        last_ind = len(nums)-1
        
        i=0
        while i<=max_vis:
            if nums[i]+i>max_vis:
                max_vis = nums[i]+i
                
            if max_vis>=last_ind:
                return True
            i+=1
        return False