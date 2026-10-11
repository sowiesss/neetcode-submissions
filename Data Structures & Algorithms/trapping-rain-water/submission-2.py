class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        if n < 3: return 0

        pre = [0] * n
        suf = [0] * n
        pre[0] = height[0]
        suf[n-1] = height[n-1]
        for i in range(1, n + 1):
            if i < n:
                pre[i] = max(height[i], pre[i - 1])
            if i > 1:
                suf[n - i] = max(height[n - i], suf[n - i + 1])
        # print(pre, '\n', suf)
        for i in range(1, n - 1):
            m = min(pre[i], suf[i])
            total += m - height[i]
        
        return total

        