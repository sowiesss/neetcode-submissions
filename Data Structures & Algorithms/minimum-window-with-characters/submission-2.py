class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tcnt = Counter(t)
        l = 0
        match = 0
        res = ""
        for r in range(len(s)):
            # print(l, r)
            if s[r] not in t:
                if l == r:
                    l += 1
                continue
            tcnt[s[r]] -= 1
            if tcnt[s[r]] == 0:
                match += 1
            # print(match, tcnt)
            if match == len(tcnt):
                while s[l] not in t or tcnt[s[l]] < 0:
                    if tcnt[s[l]] < 0:
                        tcnt[s[l]] += 1
                    l += 1
                # print(l, r)
                if len(res) == 0 or r - l + 1 < len(res):
                    res = s[l:r + 1]
                    # print(res)
                tcnt[s[l]] += 1
                match -= 1
                l += 1
                
                # print(r, l, tcnt)

                
        return res
                
