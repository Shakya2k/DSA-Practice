class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictu = {}
        for i in strs:
            if ''.join(sorted(i)) not in dictu:
                dictu[''.join(sorted(i))] = [i]
            else:
                dictu[''.join(sorted(i))].append(i)
        return dictu.values()