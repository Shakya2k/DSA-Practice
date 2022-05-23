class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = sorted(list(set(candidates)))
        ans = []
        temp = []
        self.backtracking(0,arr,temp,ans,target)
        return ans
    def backtracking(self, index, arr, temp, ans, target):
        if target == 0:
            ans.append(list(temp))
            return
        for i in range (index,len(arr)):
            if target-arr[i] >= 0:
                temp.append(arr[i])
                self.backtracking(i,arr,temp,ans,target-arr[i])
                temp.remove(arr[i])