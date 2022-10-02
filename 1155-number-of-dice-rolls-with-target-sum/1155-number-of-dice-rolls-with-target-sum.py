class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mxn=10**9 + 7
		
        dp=[[0 for i in range(target+1)] for j in range(n+1)]
        dp[0][0]=1
		
        for i in range(n+1):
            for sm in range(1,target+1):           
                if sm>k:
                    dp[i][sm]=(dp[i][sm] + dp[i-1][sm-1]-dp[i-1][sm-k-1])%mxn
                else:
                    dp[i][sm]=(dp[i][sm] + dp[i-1][sm-1])%mxn
                
                dp[i][sm]=(dp[i][sm]+dp[i][sm-1])%mxn
                
        return (dp[n][target]-dp[n][target-1])%mxn