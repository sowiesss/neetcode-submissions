class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        ma = 0
        for i in range(n):
            start = i
            while stk and stk[-1][0] >= heights[i]:
                stk.pop()
            if stk:
                h, ind = stk[-1] # h < heights[i]
                ma = max((i - ind) * h, ma)
                start = ind # save leftmost of heights[i]
            stk.append((heights[i], start))

        for h, s in stk:
            ma = max(h * (n - s), ma) # n - 1 included

        return ma