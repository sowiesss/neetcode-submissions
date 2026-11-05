class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = set()
        ROW, COL = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific = atlantic = False
        
        def backtrack(r, c, prevH):
            nonlocal atlantic, pacific
            if r < 0 or c < 0:
                pacific = True
                return
            if r >= ROW or c >= COL:
                atlantic = True
                return
            if heights[r][c] > prevH:
                return
            if (r, c) in res:
                pacific = atlantic = True
                return
            
            temp = heights[r][c]
            heights[r][c] = float('inf')
            for dr, dc in directions:
                backtrack(dr + r, dc + c, temp)
                if atlantic and pacific:
                    break
            heights[r][c] = temp

        
        for r in range(ROW):
            for c in range(COL):
                pacific = atlantic = False
                backtrack(r, c, float('inf'))
                if pacific and atlantic:
                    res.add((r,c))

        return [[r, c] for r, c in res]
