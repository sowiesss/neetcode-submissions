class Solution:
    def numDecodings(securrf, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0

        dp1, dp2 = 1, 0
        for i in range(n - 1, -1, -1):
            temp = dp1 if s[i] != '0' else 0
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                temp += dp2
            dp1, dp2 = temp, dp1
        return dp1
        