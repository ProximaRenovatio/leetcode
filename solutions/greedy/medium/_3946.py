
class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
            n = len(items)
                    min_price = min(price for _, price in items)

                            # Count the free items obtained from the first purchase of each type.
                                    gains = []
                                            for i in range(n):
                                                        factor, price = items[i]
                                                                    free_count = sum(
                                                                                    1
                                                                                                    for j in range(n)
                                                                                                                    if i != j and items[j][0] % factor == 0
                                                                                                                                )
                                                                                                                                            gains.append((price, free_count + 1))

                                                                                                                                                    # 0/1 knapsack: dp[c] = maximum items obtained by spending exactly c.
                                                                                                                                                            dp = [-1] * (budget + 1)
                                                                                                                                                                    dp[0] = 0

                                                                                                                                                                            for price, gain in gains:
                                                                                                                                                                                        for c in range(budget, price - 1, -1):
                                                                                                                                                                                                        if dp[c - price] != -1:
                                                                                                                                                                                                                            dp[c] = max(dp[c], dp[c - price] + gain)

                                                                                                                                                                                                                                    # Spend the remaining budget on the cheapest item.
                                                                                                                                                                                                                                            ans = 0
                                                                                                                                                                                                                                                    for spent in range(budget + 1):
                                                                                                                                                                                                                                                                if dp[spent] != -1:
                                                                                                                                                                                                                                                                                extra = (budget - spent) // min_price
                                                                                                                                                                                                                                                                                                ans = max(ans, dp[spent] + extra)

                                                                                                                                                                                                                                                                                                        return ans
                                                                                                                                                                                                                                                                                                        