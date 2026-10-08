from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        w = len(grid)
        h = len(grid[0])
        minute_grid = [[float('inf') for i in range(0,h)] for _ in range(0,w)]
        queue = deque()
        for i in range(0,w):
            for j in range(0, h):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                    minute_grid[i][j] = 0
        
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        while queue:
            print(queue)
            i, j, minute = queue.popleft()

            for d_i, d_j in dirs:
                new_i = i + d_i
                new_j = j + d_j
                if new_i < 0 or new_i >= w or \
                    new_j < 0 or new_j >= h:
                    continue
                
                fruit_status = grid[new_i][new_j]
                shorter = False
                if fruit_status in (1,2):
                    grid[new_i][new_j] = 2
                    if minute_grid[new_i][new_j] > minute + 1:
                       minute_grid[new_i][new_j] = minute + 1
                       shorter = True
                    if fruit_status == 1 or shorter:
                        queue.append((new_i, new_j, minute + 1)) 

        min_minute = 0
        print(minute_grid)
        print(grid)
        for i in range(0,w):
            for j in range(0,h):
                if grid[i][j] == 1:
                    return -1
                if minute_grid[i][j] !=float("inf"):
                    min_minute = max(min_minute, minute_grid[i][j])
        
        if min_minute == float("inf"):
            return -1

        return min_minute
        
        








        