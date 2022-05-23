class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisec(state):
            index = -1
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    if state == 'left':
                        right = mid - 1
                    elif state == 'right':
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index
        return [bisec('left'), bisec('right')]
        
        