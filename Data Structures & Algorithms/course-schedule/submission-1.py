class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

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
        while q:
            crs = q.pop(0)
            finish += 1
            for d in dependent[crs]:
                indegree[d] -= 1
                if not indegree[d]:
                    q.append(d)
            
        return finish == numCourses
            
        



        
        
        