class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)        
        for fr, to in tickets:
            adj[fr].append(to)
        for k in adj:
            adj[k].sort(reverse=True)

        res = []
        stk = ["JFK"]
        while stk:
            curr = stk[-1]
            if curr not in adj or not adj[curr]:
                res.append(stk.pop())
            else:
                stk.append(adj[curr].pop())

        return res[::-1]

