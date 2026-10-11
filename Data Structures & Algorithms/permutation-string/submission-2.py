class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        cnt1 = [0] * 26
        cnt2 = [0] * 26

        for i in range(len(s1)):
            cnt1[ord(s1[i]) - ord('a')] += 1
            cnt2[ord(s2[i]) - ord('a')] += 1
        
        match = 0
        for i in range(26):
            if cnt1[i] == cnt2[i]:
                match += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26:
                return True

            inr = ord(s2[r]) - ord('a')
            if cnt2[inr] == cnt1[inr]:
                match -= 1
            cnt2[inr] += 1
            if cnt2[inr] == cnt1[inr]:
                match += 1
            
            inl = ord(s2[l]) - ord('a')
            if cnt2[inl] == cnt1[inl]:
                match -= 1
            cnt2[inl] -= 1
            if cnt2[inl] == cnt1[inl]:
                match += 1
            l += 1
            
        return False



            