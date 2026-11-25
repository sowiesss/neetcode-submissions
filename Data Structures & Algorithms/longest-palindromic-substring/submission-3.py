class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return s
        if n == 2: return s if s[0] == s[1] else s[0]

        dp = [[False] * n for _ in range(n)]
        resL = 0
        start = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i) < 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    currL = j - i + 1
                    if currL > resL:
                        resL = currL
                        start = i
       
        return s[start: start + resL]


            
            
                
            
