import re
class Solution(object):
    def isPalindrome(self, s):
        su = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return su == su[::-1]
