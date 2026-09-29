class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # A valid path must contain an even number of cells.
        if (m + n - 1) % 2 == 1:
            return False

        # dp[j] contains all possible balances that can reach
        # the current cell in column j.
        dp = [set() for _ in range(n)]

        # Start at (0, 0)
        if grid[0][0] == '(':
            dp[0].add(1)
        else:
            return False

        for i in range(m):
            for j in range(n):

                # Skip the starting cell
                if i == 0 and j == 0:
                    continue

                current = grid[i][j]

                # Possible balances for this cell
                balances = set()

                # Come from the cell above
                if i > 0:
                    balances.update(dp[j])

                # Come from the cell on the left
                if j > 0:
                    balances.update(dp[j - 1])

                new_balances = set()

                for balance in balances:

                    if current == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    # A valid path can never have more closing
                    # parentheses than opening parentheses.
                    if new_balance >= 0:
                        new_balances.add(new_balance)

                dp[j] = new_balances

        # The path is valid only if the final balance is 0.
        return 0 in dp[n - 1]