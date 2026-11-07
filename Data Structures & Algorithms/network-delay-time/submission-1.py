class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if len(times) < n - 1:
            return -1

        timebook = defaultdict(list)
        
        for ui, vi, ti in times:
            timebook[ui].append((vi, ti))

        times = [math.inf] * (n + 1)
        visit = set()
        
        def dfs(node, time):
            if times[node] > time:
                times[node] = time
            else:
                return
            
            for nei, ti in timebook[node]:
                dfs(nei, time + ti)


        dfs(k, 0)
        res = 0
        for i in range(1, n + 1):
            if times[i] == math.inf:
                return -1
            if times[i] > res:
                res = times[i]

        return res



        