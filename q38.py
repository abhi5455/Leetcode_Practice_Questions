class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

# Another Solution O(n²)

# class Solution(object):
#     def maxProfit(self, prices):
#         maxDiff = 0
#         for i in range(len(prices)):
#                 if(max(prices[i:])-prices[i] > maxDiff):
#                     maxDiff = max(prices[i:])-prices[i]
#         return maxDiff
