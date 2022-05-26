class Solution:
    def jump(self, nums: List[int]) -> int:
        #We need to keep the track of the indices from which we are visiting that index and 
        #then find the minimum among them
        n = len(nums)
        visiting = [[ ] for i in range(n)]
        result = [0 for i in range(n)]
        index = 0
        while index < n:
            val = nums[index]
            for j in range(index+1,index+1+val):
                if j >= n:
                    break
                visiting[j].append(index)
            index += 1
        for i in range(1,n):
            minVal = result[visiting[i][0]]
            for j in range(len(visiting[i])):
                if minVal  > result[visiting[i][j]]:
                    minVal = result[visitng[i][j]]
            result[i] = 1 + minVal
        return result[n-1]