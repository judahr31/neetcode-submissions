class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0;

        islands = 0

        def dfs(row, column):
            if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] == '0':
                return

            grid[row][column] = "0"

            dfs(row-1, column)
            dfs(row+1, column)
            dfs(row, column-1)
            dfs(row, column+1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
                    
        return islands 