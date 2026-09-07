class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        
        last = {}
        
        for i in range(1, n + 1):
            current = s[i - 1]
            
            dp[i] = 2 * dp[i -1]
        
            if current in last:
                k = last[current]
                dp[i] -= dp[k - 1]
             
            dp[i] %= MOD   
            last[current] = i
            
        return (dp[n] - 1) % MOD