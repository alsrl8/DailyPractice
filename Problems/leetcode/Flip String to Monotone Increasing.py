class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [[0, 0] for i in range(n)]

        if s[0] == "1":
            dp[0][0] = 1
        
        for i in range(1, n):
            num = s[i]
            if num == "0":
                dp[i][0] = dp[i-1][0]
                dp[i][1] = min(dp[i-1][0], dp[i-1][1] + 1)
            else:   # num == "1"
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1]
        
        return min(dp[n-1][0], dp[n-1][1])
    
    def minFlipsMonoIncr_improved(self, s: str) -> int:
        dp, c = 0, 0
        
        for num in s:
            if num == "0":
                dp = min(c, dp+1)
            else:   # num == "1"
                c += 1
        
        return dp
