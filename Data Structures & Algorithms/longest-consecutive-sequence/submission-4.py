class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in num_set:
                cnt = 1
                while n + cnt in num_set:
                    cnt += 1
                        
                longest = max(cnt, longest)
            return longest