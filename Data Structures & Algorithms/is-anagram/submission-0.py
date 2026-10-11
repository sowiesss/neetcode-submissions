class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tlist = list(t)
        for char in s:
            if char in tlist:
                tlist.remove(char)
            else:
                return False
        
        return len(tlist) == 0
            