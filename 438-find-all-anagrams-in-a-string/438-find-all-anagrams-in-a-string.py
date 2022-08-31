class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount = Counter(p)
        pLen = len(p)
        sCount = Counter(s[:pLen])
        
        res = []
        for i in range(len(s) - pLen + 1):
            if pCount == sCount:
                res.append(i)
            sCount[s[i]] -= 1
            if i + pLen in range(len(s)):
                sCount[s[i + pLen]] += 1
        return res
        