class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        elif len(s) != 0 and s[0] not in t:
            return False
        if len(s) <= 1:
            return s in t
        return self.isSubsequence(s[1:], t[t.index(s[0])+1:])
        