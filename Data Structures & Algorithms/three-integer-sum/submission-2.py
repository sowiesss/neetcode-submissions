class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        leng = len(nums)
        count = Counter(nums)
        res = []
        for i, n in enumerate(nums):
            if i > leng - 2: 
                break
            if n > 0: 
                break
            
            count[n] -= 1 #must before dup check
            if i > 0 and n == nums[i - 1]:
                continue
            
            for j in range(i + 1, leng):
                count[nums[j]] -= 1
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target = - nums[i] - nums[j]

                if count[target] > 0:
                    res.append([n, nums[j], target])
                
            for j in range(i + 1, leng):
                count[nums[j]] += 1

        return res

