class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_cost = 0, float('inf')
        for i in range(len(prices)):
            profit = prices[i] - min_cost
            max_profit = max(max_profit, profit)
            min_cost = min(prices[i], min_cost)
        return max_profit