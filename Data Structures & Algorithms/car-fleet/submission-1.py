class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True) # descending

        cnt = 0
        prev_t = 0

        for p, s in pairs:
            t = (target - p) / s
            if (prev_t and t > prev_t) or not prev_t:
                prev_t = t
                cnt += 1
                

        return cnt


