class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1, len1 = Counter(s1), len(s1)
        match = 0
        
        if len1 > len(s2): return False

        for i in range(len1):
            if s2[i] in cnt1:
                if cnt1[s2[i]] == 0: match -= 1
                cnt1[s2[i]] -= 1
                if cnt1[s2[i]] == 0: match += 1

        if match == len(cnt1):
            return True

        for i in range(len1, len(s2)):
            # if s2[i] in cnt1:
            l = i - len1
            # print(i, l, match, cnt1)
            if s2[i] in cnt1:
                if cnt1[s2[i]] == 0: match -= 1
                cnt1[s2[i]] -= 1
                if cnt1[s2[i]] == 0: match += 1

            if s2[l] in cnt1:
                if cnt1[s2[l]] == 0: match -= 1
                cnt1[s2[l]] += 1
                if cnt1[s2[l]] == 0: match += 1

            if match == len(cnt1):
                return True
            
        return False