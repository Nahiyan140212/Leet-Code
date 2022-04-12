class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for i in prices:
            min_price = min(min_price, i)
            potential_profit = i - min_price
            max_profit = max(max_profit, potential_profit)
        return max_profit
            
#Different Approach

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r+=1
        return max_profit
            
