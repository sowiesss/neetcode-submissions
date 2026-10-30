class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        self.nums = nums
        for n in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, n)
            elif n > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, n)


    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        self.nums.append(val)
        
        return self.heap[0]

        
