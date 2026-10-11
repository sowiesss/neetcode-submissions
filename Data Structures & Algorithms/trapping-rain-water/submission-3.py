class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        l, r = 0, n - 1
        lmax, rmax = height[l], height[r]

        while l < r:
            if lmax <= height[l]:
                lmax = height[l]
            if rmax <= height[r]:
                rmax = height[r]
            if lmax < rmax:
                total += lmax - height[l]
                l += 1
            else:
                total += rmax - height[r]
                r -= 1

        return total

        