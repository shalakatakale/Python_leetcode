#1
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum1 = 0
        for i in range(len(s)):
            sum1 = sum1*26 + (ord(s[i])-65+1)
        return sum1

#2
def titleToNumber(self, s):
    return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))