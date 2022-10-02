class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        oneBack = 1
        twoBack = 1
        for i in range(1, len(s)):
            cur = 0
            if s[i] != '0':
                cur += oneBack
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                cur += twoBack
            oneBack, twoBack = cur, oneBack
        return oneBack