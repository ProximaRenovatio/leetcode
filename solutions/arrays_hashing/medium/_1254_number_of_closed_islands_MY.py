
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        tabu = [[False for _ in range(m)] for _ in range(n)]
        res = 0

        way = {
            0: (-1, 0),
            1: (0, -1),
            2: (1, 0),
            3: (0, 1)
        }

        def search(r: int, c: int) -> bool:
            tabu[r][c] = True

            # An island touching the border is not closed
            closed = r != 0 and r != n - 1 and c != 0 and c != m - 1

            for dr, dc in way.values():
                nr = r + dr
                nc = c + dc

                if (0 <= nr < n and 0 <= nc < m
                        and grid[nr][nc] == 0
                        and not tabu[nr][nc]):

                    neighbor_closed = search(nr, nc)
                    closed = closed and neighbor_closed

            return closed

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and not tabu[i][j]:
                    if search(i, j):
                        res += 1

        return res