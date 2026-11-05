class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))

        dependent = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for c, pre in prerequisites:
            dependent[pre].append(c)
            indegree[c] += 1

        q = []
        for i in range(numCourses):
            if not indegree[i]:
                q.append(i)

        finish = 0
        res = []
        while q:
            crs = q.pop(0)
            res.append(crs)
            finish += 1
            for d in dependent[crs]:
                indegree[d] -= 1
                if not indegree[d]:
                    q.append(d)

        if finish == numCourses:
            return res
        else:
            return []
            
        



        
        
        