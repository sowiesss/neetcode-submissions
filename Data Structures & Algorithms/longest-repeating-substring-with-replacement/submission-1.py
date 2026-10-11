class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k + 1:
            return n

        chars = set(s)
        res = 0
        for c in chars:
            count = l = 0
            for r in range(n):
                if s[r] != c:
                    count += 1 # of replacement
                if r - l + 1 - count > k:
                    if s[l] != c:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)


        return res

        