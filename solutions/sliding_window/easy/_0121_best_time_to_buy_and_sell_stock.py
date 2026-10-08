class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        res = 0
        
        for sell in prices[1:]:
            res = max(res, sell - buy)
            buy = min(buy, sell)
            
        return res
