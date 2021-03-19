'''520 Detect capital - HELLO, Hello, hello are allowed, rest are wrong'''

class Solution(object):
    def detectCapitalUse(self, word):
        count = 0
        for i in range(len(word)):
            if word[i] >= chr(65) and word[i] < chr(91):
                count = count +1
        if count == len(word):
            return print('True')
        elif count == 0:
            return True
        elif count == 1 and word[0] >= chr(65) and word[0] < chr(91):
            return print('True')
        else:
            return print('False')

Solution().detectCapitalUse("hello")