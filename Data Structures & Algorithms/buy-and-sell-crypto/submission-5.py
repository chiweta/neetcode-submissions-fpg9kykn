class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       profit=0
       lowestval=prices[0]
       for current in prices:
           if current < lowestval:
               lowestval=current
           profit=max(profit, current - lowestval)
       return profit