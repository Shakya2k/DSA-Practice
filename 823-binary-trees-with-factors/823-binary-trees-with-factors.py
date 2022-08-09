class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        
        moduler = (10**9 +7)
    
        dp = {}
        for i in arr:
            dp[i] = 1
        
        for i,n in enumerate(arr):
            for j in range (i):
                if not(n%arr[j]) and n//arr[j] in dp:
                    dp[n] += dp[arr[j]] * dp[n//arr[j]]
                    dp[n] %= moduler
        
        return sum(dp.values())%moduler