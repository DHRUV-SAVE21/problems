class Solution(object):
    def reverseVowels(self, s):
        vowels=set('aeiouAEIOU')
        vo=list(s)
        i,j=0,len(s)-1

        while i<j:
            if vo[i] not in vowels:
                i+=1
            elif  vo[j] not in vowels:
                j-=1
            else:
                vo[i],vo[j]=vo[j],vo[i]
                i+=1
                j-=1
            
        return ''.join(vo)