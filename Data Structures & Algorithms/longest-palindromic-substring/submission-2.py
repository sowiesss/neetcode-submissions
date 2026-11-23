class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return s
        if n == 2: return s if s[0] == s[1] else s[0]
        # n > 2
        resL = 1
        start = 0

        def is_palidrome(l, r):
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    r += 1
                    l -= 1
                else:
                    compare(l, r)
                    return
            compare(l, r)


        def compare(l, r):
            nonlocal resL, start
            leng = r - l - 1
            if leng > resL:
                print(l, r)
                resL = leng
                start = l + 1
                print(resL, start)
        

        for i in range(n):
            if i < n - 1:
                is_palidrome(i, i + 1)
                if i >= 1:
                    print("odd")
                    is_palidrome(i - 1, i + 1)
        
        return s[start: start + resL]


            
            
                
            
