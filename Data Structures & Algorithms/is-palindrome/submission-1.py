class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1: return True 

        alnum = [c.lower() for c in s if c.isalnum()]
        n = len(alnum)
        print(n)
        if n == 1: return True

        if n % 2 == 0:
            i = n//2 - 1
            j = n//2
            print("%2", i, j)
            while i > 0 and j < n - 1and alnum[i] == alnum[j]:
                i -= 1
                j += 1
            if i == 0 and j == n-1 and alnum[i] == alnum[j]:
                return True
        else: # n >= 3
            i = n//2
            j = i + 1
            i = i - 1
            while i > 0 and j < n - 1 and alnum[i] == alnum[j]:
                i -= 1
                j += 1
            print(i, j)
            if i == 0 and j == n-1 and alnum[i] == alnum[j]:
                return True

        return False

