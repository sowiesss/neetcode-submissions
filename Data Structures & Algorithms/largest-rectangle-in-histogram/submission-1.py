class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        stk = []

        for i in range(n):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)

        stk = []
        for i in range(n - 1, -1, -1):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1] # else default n, to the end
            stk.append(i)

        ma = 0
        for i in range(n):
            ma = max(ma, (right[i] - left[i] - 1) * heights[i])
        
        return ma
