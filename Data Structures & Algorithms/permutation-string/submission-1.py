class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        cnt1 = Counter(s1)
        l = 0
        cnt2 = defaultdict(int)
        for r in range(len(s2)):
            if s2[r] in s1:
                cnt2[s2[r]] += 1
                while cnt2[s2[r]] > cnt1[s2[r]]:
                    cnt2[s2[l]] -= 1
                    l += 1
                if cnt2 == cnt1:
                    return True     
            else:
                cnt2 = defaultdict(int)
                l = r + 1
            
        return False



            