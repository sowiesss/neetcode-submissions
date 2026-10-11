class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True) # descending

        stk = []

        for p, s in pairs:
            t = (target - p) / s
            if (stk and t > stk[-1]) or not stk:
                stk.append(t)

        return len(stk)


