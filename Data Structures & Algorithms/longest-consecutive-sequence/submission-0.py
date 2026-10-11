class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for n in nums:
            num_set.add(n)
        
        longest = 0
        for n in nums:
            if n - 1 in num_set:
                continue
            cnt = 1
            for i in range(1, len( nums)) :
                if n + i in num_set:
                    cnt += 1
            longest = cnt if cnt > longest else longest

        return longest
