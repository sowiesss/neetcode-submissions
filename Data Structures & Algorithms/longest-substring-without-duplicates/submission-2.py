class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        leng = 0
        l, r = 0, 1
        while r < n:
            if s[r] in s[l:r]:
                while l < r and s[l] != s[r]:
                        l += 1
                l += 1
            r += 1
            leng = max(leng, r - l)

        return leng