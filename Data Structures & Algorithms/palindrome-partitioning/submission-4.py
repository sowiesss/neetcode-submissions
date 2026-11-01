class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for l in range(1, n + 1): # length of substring
            for i in range(n - l + 1): # starting ind
               dp[i][i + l - 1] = (s[i] == s[i + l - 1] 
               and ((i + 1 >= (i + l - 2)) or dp[i + 1][i + l -2]))

        def dfs(i):
            if i >= n:
                return [[]]
            
            ret = []
            for j in range(i, n):
                if dp[i][j]:
                    part = dfs(j + 1)
                    for p in part:
                        curr = [s[i: j + 1]] + p
                        ret.append(curr)
            return ret
            

        return dfs(0)


    
    