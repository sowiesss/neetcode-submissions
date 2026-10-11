class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_set = set(s)
        t_set = set(t)
        if len(s) != len(t):
            return False

        tlist = list(t)
        for char in s:
            if char in tlist:
                tlist.remove(char)
            else:
                return False
        
        return len(tlist) == 0
            