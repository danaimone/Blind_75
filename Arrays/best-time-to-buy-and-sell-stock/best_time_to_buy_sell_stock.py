def max_profit(prices: list[int]) -> int:
    max_profit, min_cost = 0, float('inf')
    for i in range(len(prices)):
        profit = prices[i] - min_cost
        max_profit = max(max_profit, profit)
        min_cost = min(prices[i], min_cost)
    return max_profit


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
