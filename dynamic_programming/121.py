# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def max_profit(prices: list) -> int:
    """Return the maximum profit for buy and sell stock
    speed: O(n)
    memory: O(1)

    prices: list[int]
    rtype: int
    """
    current_min = prices[0]
    profit = 0

    for price in prices:
        if price < current_min:
            current_min = price
        if price - current_min > profit:
            profit = price - current_min

    return profit
