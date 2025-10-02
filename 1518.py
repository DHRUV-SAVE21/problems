# 1518. Water Bottles
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total_drink=0
        full=numBottles
        empty=0

        while full>0:
            total_drink +=full
            empty +=full
            full=empty//numExchange
            empty=empty%numExchange

        return total_drink