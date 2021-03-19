'''#28 implement str str'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle==None:
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1