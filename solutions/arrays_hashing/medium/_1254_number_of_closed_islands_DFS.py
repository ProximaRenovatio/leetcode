
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= n or c < 0 or c >= m:
                return
            if grid[r][c] == 1:
                return

            # Mark this land cell as visited
            grid[r][c] = 1

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # Remove every island connected to the border
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for j in range(m):
            dfs(0, j)
            dfs(n - 1, j)

        # Count the remaining islands
        res = 0

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == 0:
                    res += 1
                    dfs(i, j)

        return res
