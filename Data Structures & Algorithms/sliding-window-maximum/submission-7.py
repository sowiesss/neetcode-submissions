class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []
        l = r = 0

        for i in range(len(nums)):
            while d and nums[i] > nums[d[-1]]:
                d.pop()
            d.append(nums[i])
            if i > k - 1:
                # print(i, d)
                l = i - k
                if d[0] == nums[l]: # i - k + 1, i
                    d.popleft()
                res.append(nums[d[0]])
            elif i == (k - 1):
                # print("18", i, d)
                res.append(d[0])
                # print(res)
        
        return res