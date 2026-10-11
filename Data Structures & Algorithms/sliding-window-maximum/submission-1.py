class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n

        pref[0] = nums[0]
        suff[-1] = nums[-1]

        for i in range(1, n):
            if i % k == 0:
                pref[i] == nums[i]
            else:
                pref[i] = max(pref[i - 1], nums[i])
            j = n - 1 - i # (0, n - 2)
            if j % k == 0:
                suff[j] = nums[j]
            else:
                suff[j] = max(suff[j + 1], nums[j])

        res = [0] * (n - k + 1)
        for i in range(n - k + 1): # (0, n - k)
            res[i] = max(pref[i + k - 1], suff[i]) # i, i+k-1
        return res
        



        