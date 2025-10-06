# 3100. Water Bottles II
class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        total = numBottles
        empty = numBottles
        while empty >= numExchange:
            empty -= numExchange
            numExchange += 1
            total += 1
            empty += 1 
        return total
