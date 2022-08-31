class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        dic = [0 for i in range(26)]
        
        while r < len(s):
            start, end = s[l:l+1], s[r:r+1]
            dic[ord(end) - ord('A')] += 1
            
            if max(dic) + k < r - l + 1:
                dic[ord(start) - ord('A')] -= 1
                l += 1
            
            r += 1
        
        return r - l