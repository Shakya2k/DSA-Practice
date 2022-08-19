class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        hashmap = {}
        
        for i in range (len(s)):
            if s[i] not in hashmap.keys() and t[i] not in hashmap.values():
                hashmap[s[i]] = t[i]
            elif s[i] not in hashmap.keys() and t[i] in hashmap.values():
                return False
            elif s[i] in hashmap.keys() and t[i] not in hashmap.values():
                return False
            elif hashmap[s[i]] != t[i]:
                return False
        return True
        

        