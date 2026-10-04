import heapq

class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:

        min_time_grid = [[2 ** 31] * len(grid[i]) for i in range(0, len(grid))]
        min_time_grid[0][0] = grid[0][0]
        direction = [(0,1), (0,-1), (1,0), (-1,0)]
        heap = [(min_time_grid[0][0],0,0)]
        while heap:
            t, x, y = heapq.heappop(heap)
            loc = (x,y)
            print(loc, t)
            if t > min_time_grid[loc[0]][loc[1]]:
                continue
            for d in direction:
                i,j = (loc[0] + d[0], loc[1] + d[1])

                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                    continue
                new_t = max(t,grid[i][j])
                if new_t >= min_time_grid[i][j]:
                    continue
                min_time_grid[i][j] = new_t

                heapq.heappush(heap,(new_t, i, j))
        
        return min_time_grid[-1][-1]
        