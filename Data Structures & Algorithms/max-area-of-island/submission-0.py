from collections import deque

class Solution:

    checked = None
    class Blob:
        def __init__(self):
            self.size = 0
        
        def expand(self, grid, i, j, checked):
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            w, h = len(checked), len(checked[0])
            queue = deque()
            queue.append((i,j))

            while queue:
                self.size += 1
                i, j = queue.popleft()
                for x,y in dirs:

                    new_i = i + x
                    new_j = j + y

                    if not (0<=new_j<h) or not (0<=new_i<w):
                        continue
                    
                    if grid[new_i][new_j] == 1 and not checked[new_i][new_j]:
                        queue.append((new_i,new_j))

                    checked[new_i][new_j] = True


            

            
            
            

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        checked = [[False] * len(grid[0]) for i in range(0,len(grid))]
        max_area = 0

        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1 and not checked[i][j]:
                    checked[i][j] = True
                    blob = self.Blob()
                    blob.expand(grid,i,j, checked)
                    max_area = max(max_area, blob.size)
                checked[i][j] = True
        
        return max_area




        