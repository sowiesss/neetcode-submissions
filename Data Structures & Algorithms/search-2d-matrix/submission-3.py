class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        r1, r2 = 0, m - 1

        while r1 <= r2:
            mid = r1 + (r2 - r1) // 2
            if matrix[mid][0] > target:
                r2 = mid - 1
            elif matrix[mid][-1] < target:
                r1 = mid + 1
            else:
                break
        
        r = mid
        c1, c2 = 0, n - 1
        while c1 < c2:
            mid = c1 + (c2 - c1) // 2
            if matrix[r][mid] < target:
                c1 = mid + 1
            elif matrix[r][mid] > target:
                c2 = mid - 1
            else:
                return True
        
        return False

        

    
