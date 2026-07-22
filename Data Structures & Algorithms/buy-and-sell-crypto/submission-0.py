class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        left = 0          # Buy day
        right = 1         # Sell day
        max_profit = 0

        while right < len(prices):

            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # Found a cheaper buying price
                left = right

            right += 1

        return max_profit