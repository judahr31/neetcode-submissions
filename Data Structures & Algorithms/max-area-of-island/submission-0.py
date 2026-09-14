class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_island = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            current_area = 1
            current_area += dfs(r-1, c)
            current_area += dfs(r+1, c)
            current_area += dfs(r, c-1)
            current_area += dfs(r, c+1)

            return current_area


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_island = max(area, max_island)

        return max_island


            