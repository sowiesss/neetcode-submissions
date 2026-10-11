class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True) # descending

        fleet = 1
        prev_t = (target - pairs[0][0]) / pairs[0][1]

        for i in range(1, len(pairs)):
            p, s = pairs[i]
            t = (target - p) / s
            if t > prev_t:
                fleet += 1
                prev_t = t 

        return cnt


