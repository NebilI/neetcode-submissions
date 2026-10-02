class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        num_islands = 0
        queue = []
        for i in range(0, len(grid)):
            for j, val in enumerate(grid[i]):
                if val != "1":
                    continue
                num_islands += 1
                queue = [(i,j)]
                while len(queue) > 0:
                    t_i, t_j = queue.pop(0)
                    for c_i, c_j in ((t_i + 1, t_j), (t_i - 1, t_j), (t_i, t_j - 1), (t_i, t_j + 1)):
                        if c_i >= 0 and c_i < len(grid) and c_j >= 0 and c_j < len(grid[c_i]) and \
                            grid[c_i][c_j] == "1":
                            grid[c_i][c_j] = "2"
                            queue.append((c_i, c_j))

        return num_islands


                

                

        