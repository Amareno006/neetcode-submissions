class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_day = prices[0]
        max_day = 0
        for p in range(len(prices) -1):
            min_day = min(min_day,prices[p])
            max_profit = max(max_profit, max(0, prices[p+1] - min_day))
        print(max_profit)

        return max_profit

