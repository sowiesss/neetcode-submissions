class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        ma = 0
        for i in range(n):
            while stk and heights[stk[-1]] >= heights[i]: # reached end, pop all remaining in stk or h[i] <= h[stk[-1]], pop heigher bars
                h = heights[stk.pop()]
                l = stk[-1] if stk else -1 # h[i] <= h but we are calculating for h not h[i], so i, l not included, h[i] will be calculated when i is poped; if not stk, then 0 included
                ma = max(ma, (i - l - 1) * h)
        
            stk.append(i)

        for i, ind in enumerate(stk):
            h = heights[ind]
            l = stk[i - 1] if i > 0 else -1 # else include l
            ma = max(ma, (n - l - 1) * h) # n, l excluded
            
        return ma