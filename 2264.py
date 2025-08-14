
#2264. Largest 3-Same-Digit Number in String
class Solution(object):
    def largestGoodInteger(self, num):
        large=""

        for i in range(len(num)-2):
            three_digit=num[i:i+3]
            
            if three_digit[0]==three_digit[1]==three_digit[2]:
                if three_digit>large:
                    large=three_digit
                
        return large
