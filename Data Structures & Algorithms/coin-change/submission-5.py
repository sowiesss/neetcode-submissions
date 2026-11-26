class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
       
        seen = [0] * amount
        q = deque([0])
        cnt = 0
        while q:
            for _ in range(len(q)):
                a = q.popleft()
                for c in coins:
                    s = a + c
                    if s == amount:
                        return cnt + 1
                    if s < amount and not seen[s]:
                        q.append(s)
            cnt += 1

        return -1
            
            
        