class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                target = - nums[i]
                # print('1', j, k)
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                # print('2', j, k)
                if j < k:
                    s = nums[j] + nums[k]
                    if s < target:
                        j += 1
                    elif s > target:
                        k -= 1
                    else:
                        # print('3', j, k)
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        # print('4', j, k)
        return res

