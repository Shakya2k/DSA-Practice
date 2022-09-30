class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diffs = [(abs(n-x), i) for (i, n) in enumerate(arr)]
        diffs.sort()
        result = [arr[i[1]] for i in diffs[:k]]
        return sorted(result)