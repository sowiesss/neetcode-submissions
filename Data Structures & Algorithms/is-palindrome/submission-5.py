class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if len(s) <= 1: return True 
        alnum = [c.lower() for c in s if c.isalnum()]
        return alnum == alnum[::-1]

        

