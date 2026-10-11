class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        cnt1 = Counter(s1)
        match = 0

        for i in range(len(s1)):
            if s2[i] in cnt1:
                if cnt1[s2[i]] == 0: 
                    match -= 1
                cnt1[s2[i]] -= 1
                if cnt1[s2[i]] == 0: 
                    match += 1
        
        if match == len(cnt1):
            return True

        for r in range(len(s1), len(s2)):
            if s2[r] in cnt1:
                if cnt1[s2[r]] == 0:
                    match -= 1
                cnt1[s2[r]] -= 1
                if cnt1[s2[r]] == 0:
                    match += 1
            
            l = i - len(s1)
            if s2[l] in cnt1:
                if cnt1[s2[l]] == 0:
                    match -= 1
                cnt1[s2[l]] += 1
                if cnt1[s2[l]] == 0:
                    match += 1
            l += 1

            if match == len(cnt1):
                return True
            
        return False



            