class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        def valid(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        
        def palindrome(part: List[str], start: int):
            if start >= n:
                res.append(part.copy())
                return
            
            for i in range(start, n):
                if dp[start][i]:
                    part.append(s[start:i + 1])
                    palindrome(part, i + 1)
                    part.pop()
        

        for l in range(1, n + 1): # length of substring
            for i in range(n - l + 1): # starting ind
               dp[i][i + l - 1] = (s[i] == s[i + l - 1] 
               and ((i + 1 >= (i + l - 2)) or dp[i + 1][i + l -2]))

        palindrome([], 0)
        return res