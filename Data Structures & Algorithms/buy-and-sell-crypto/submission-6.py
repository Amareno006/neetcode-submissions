class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = []
        min_day = prices[0]
        max_day = 0
        for p in range(len(prices) -1):
            min_day = min(min_day,prices[p])
            max_profit.append(max(0, prices[p+1] - min_day))
        print(max_profit)
        if not max_profit: 
            return 0
        return max(max_profit)

