class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""
        if len(s) == len(t):
            return s if Counter(s) == Counter(t) else ""


        tcnt = Counter(t)
        l = 0
        match = 0
        res = ""
        for r in range(len(s)):#
            if s[r] in t:
                tcnt[s[r]] -= 1
                if tcnt[s[r]] == 0: # ignore < 0
                    match += 1
                if match == len(tcnt):
                    while s[l] not in t or tcnt[s[l]] < 0:
                    # move start to shrink window
                        if s[l] in t:
                            tcnt[s[l]] += 1
                        l += 1

                    if not res or r - l + 1 < len(res):
                        res = s[l:r + 1]
                    tcnt[s[l]] += 1
                    match -= 1
                    l += 1
                
        return res