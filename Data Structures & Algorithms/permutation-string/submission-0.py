class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        cnt1 = Counter(s1)
        l = 0
        for r in range(len(s2)):
            # print(r, cnt1)
            if s2[r] not in cnt1:
                while l < r:
                    cnt1[s2[l]] += 1
                    l += 1
                l += 1
                continue
            cnt1[s2[r]] -= 1
            # print(r, cnt1)
            if cnt1[s2[r]] == 0:
                res = True
                # print(r, cnt1)
                for c, count in cnt1.items():
                    # print(c, count)
                    if count != 0:
                        res = False
                        break
                if res:
                    return True
            while cnt1[s2[r]] < 0:
                cnt1[s2[l]] += 1
                l += 1
        return False



            