class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0
        sell_index = 1
        running_max = 0
        while sell_index < len(prices):
            if prices[buy_index] < prices[sell_index]:
                profit = prices[sell_index] - prices[buy_index]
                running_max = max(running_max, profit)
            else:
                buy_index = sell_index

            sell_index += 1
        
        return running_max