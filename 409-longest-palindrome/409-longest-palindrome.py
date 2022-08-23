class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = Counter(s)
        even , odd = 0, 0
        for i in dic:
            if dic[i]%2==0:
                even += dic[i]
            else:
                odd += (dic[i] -1)
        hasOdd = any(dic[i] %2==1 for i in dic)
        return even + odd + hasOdd