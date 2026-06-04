class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_day = prices[0]
        for p in range(len(prices)):
            max_profit = max(max_profit, prices[p] - min_day)
            min_day = min(min_day,prices[p])

        return max_profit

