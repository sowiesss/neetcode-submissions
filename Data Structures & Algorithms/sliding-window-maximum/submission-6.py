class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []
        l = r = 0

        for i in range(len(nums)):
            while d and nums[i] >= nums[d[-1]]:
                d.pop()
            d.append(i)
            if i >= k - 1:
                while d[0] <= i - k: # i - k + 1, i
                    d.popleft()
                res.append(nums[d[0]])
        
        return res