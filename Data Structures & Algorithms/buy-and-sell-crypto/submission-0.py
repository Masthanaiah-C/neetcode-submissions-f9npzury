class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        sell = prices[0]
        buy = prices[0]
        profit = 0
        for i in prices:
            if (i> sell):
                sell = i
            
            profit = max(profit, sell - buy )
            if (i < buy):
                buy = i
                sell = i
        return profit
        