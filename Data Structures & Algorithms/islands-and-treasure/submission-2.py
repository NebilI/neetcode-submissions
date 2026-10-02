class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        to_look = collections.deque()
        width = len(grid[0])
        height = len(grid)

        for i in range(0, height):
            for j in range(0, width):
                if grid[i][j] == 0:
                    to_look.append((i,j))

        while len(to_look) > 0:
            i,j = to_look.popleft()
            val = grid[i][j]
            if i - 1 >= 0:
                check = grid[i - 1][j]
                if val + 1 < check and check > 0:
                    grid[i - 1][j] = val + 1
                    to_look.append((i-1,j))
            if i < height - 1:
                check = grid[i + 1][j]
                if val + 1 < check and check > 0:
                    grid[i + 1][j] = val + 1
                    to_look.append((i+1,j))     
            if j - 1 >= 0:
                check = grid[i][j - 1]
                if val + 1 < check and check > 0:
                    grid[i][j - 1] = val + 1
                    to_look.append((i,j - 1))
            if j < width - 1:
                check = grid[i][j + 1]
                if val + 1 < check and check > 0:
                    grid[i][j + 1] = val + 1
                    to_look.append((i,j + 1))

            