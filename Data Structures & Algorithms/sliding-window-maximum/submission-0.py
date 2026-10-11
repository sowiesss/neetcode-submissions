class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i in range(k):
            heapq.heappush(heap, (- nums[i], i))
        res.append(- heap[0][0])
        
        for r in range(k, len(nums)):
            heapq.heappush(heap, (- nums[r], r))
            l = r - k # to remove
            while heap[0][1] <= l:
                heapq.heappop(heap)
            res.append(- heap[0][0])
        return res
        



        