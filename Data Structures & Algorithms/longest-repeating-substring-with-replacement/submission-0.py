class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k + 1:
            return n

        count = defaultdict(int)
        maxf = res = l = 0

        for r in range(n):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            while r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

        