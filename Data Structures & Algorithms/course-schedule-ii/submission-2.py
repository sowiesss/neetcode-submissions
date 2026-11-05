class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))

        preMap = {i : [] for i in range(numCourses)}
        for c, pre in prerequisites:
            preMap[c].append(pre)
        visited = set()
        res = []

        def dfs(crs, path):
            if crs in path:
                return False
            if crs in visited:
                return True
            path.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre, path):
                    return False
            path.remove(crs)
            res.append(crs)
            visited.add(crs)
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return []
           
        return res



        
        
        