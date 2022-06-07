class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        
        result = []
        hash_map = {}
        for i in range(len(nums)) :
            j = i+1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0 and j != k :
                    if str(nums[i])+'_'+str(nums[j]) not in hash_map : 
                        result.append([nums[i], nums[j], nums[k]])
                        hash_map[str(nums[i])+'_'+str(nums[j])] = nums[k]
                    k -= 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0 : 
                    k -= 1
                else :
                    j+= 1
                        
        return result
                        
                
            