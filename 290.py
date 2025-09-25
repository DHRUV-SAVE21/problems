# 290. Word Pattern
class Solution(object):
    def wordPattern(self, pattern, s):
        words=s.split()
        if len(pattern)!=len(words):
            return False

        cha_to_wo={}
        wo_to_cha={}
        for c,w in zip(pattern,words):
            if c in cha_to_wo and cha_to_wo[c]!=w:
                return False
            if w in wo_to_cha and wo_to_cha[w]!=c:
                return False
            
            cha_to_wo[c]=w
            wo_to_cha[w]=c
        return True

        