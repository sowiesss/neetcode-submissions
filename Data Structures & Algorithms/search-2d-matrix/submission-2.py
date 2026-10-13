class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        top, bot = 0, ROW - 1

        while top <= bot:
            mid = top + (bot - top) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                break # find the row

        row = mid
        l, r = 0, COL - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True 
        
        return False
