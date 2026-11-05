class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        preMap = {i : [] for i in range(numCourses)}
        for c, pre in prerequisites:
            preMap[c].append(pre)

        def dfs(crs, pres, path):
            if crs in path:
                return False
            if pres == []:
                return True

            path.add(crs)
            for pre in pres:
                if not dfs(pre, preMap[pre], path):
                    return False
            path.remove(crs)
            preMap[crs] = []
            return True

        
        for crs, pres in preMap.items():
            if not dfs(crs, pres, set()):
                return False
        return True


        
        
        