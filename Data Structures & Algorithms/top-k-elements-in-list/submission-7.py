class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq =[[] for i in range(len(nums)+1)]
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



