class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))

        adj = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for c, pre in prerequisites:
            adj[pre].append(c)
            indegree[c] += 1

        res = []

        def dfs(crs):
            res.append(crs)
            indegree[crs] = -1
            for d in adj[crs]:
                indegree[d] -= 1
                if not indegree[d]:
                    dfs(d)


        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
                
        return res if len(res) == numCourses else []
        


        
        
        