class Solution(object):
    def maxProfit(self, prices):
        min=float('inf')
        max=0

        for price in prices:
            if price < min:
                min=price
            else:
                profit=price-min
                if profit>max:
                    max=profit
        return max
        