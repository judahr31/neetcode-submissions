class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]

        max_profit = 0

        for idx, price in enumerate(prices):
            if low > price:
                low = price
            else:
                if (price - low) > max_profit:
                    max_profit = price - low
        
        return max_profit
        