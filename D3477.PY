#3477. Fruits Into Baskets II
#fruits=[4,2,5]
#baskets=[3,5,4]
class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        count = 0
        
        for num in fruits:
            for j in range(len(baskets)):
                if baskets[j] >= num:
                    baskets[j] = 0
                    count += 1
                    break
        return len(fruits) - count
    

