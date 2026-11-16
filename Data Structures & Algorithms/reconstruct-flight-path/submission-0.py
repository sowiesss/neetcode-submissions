class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)        
        for fr, to in tickets:
            adj[fr].append(to)
        for k in adj:
            adj[k].sort()

        vertice = len(tickets) + 1
        res = ['JFK']

        def dfs(start):
            if len(res) == vertice:
                return True
            if start not in adj:
                return False
            
            for i, v in enumerate(adj[start]):
                adj[start].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                res.pop()
                adj[start].insert(i, v)

        dfs('JFK')
        return res

