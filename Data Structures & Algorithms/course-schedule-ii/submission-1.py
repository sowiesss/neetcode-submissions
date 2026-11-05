class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))

        preMap = {i : [] for i in range(numCourses)}
        for c, pre in prerequisites:
            preMap[c].append(pre)

        res = []

        def dfs(crs, path):
            if crs in path:
                return False
            path.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre, path):
                    return False
            path.remove(crs)
            preMap[crs] = []
            return True

        for i in range(numCourses):
            if dfs(i, set()):
                res.append(i)
            
        if len(res) == numCourses:
            return res
        else:
            return []



        
        
        