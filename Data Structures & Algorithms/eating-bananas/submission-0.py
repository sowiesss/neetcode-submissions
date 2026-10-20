class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            total = 0
            for p in piles:
                total += math.ceil(p / speed)

            if total <= h:
                return speed
            speed += 1
        
        return -1