'''#58 Length of last word
# I have only used split and not split'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = []
        if " " in s:
            words = s.split()
            if words:
                return len(words[-1])
            else:
                return 0
        else:
            return len(s)

# 2
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])

# 3
class Solution:
    def lengthOfLastWord(self, s):
        a = s.split()

        if len(a) > 0:
            av = a[-1]
            return(len(av))

        return 0