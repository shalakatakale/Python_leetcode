'''5. Longest Palindromic Substring  - String, Dynamic Programming'''
class Solution(object):
    # Helper function
    def checkPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    def longestPalindrome(self, s):
        result = ""
        for i in range(len(s)):
            word1 = self.checkPalindrome(s, i, i)
            word2 = self.checkPalindrome(s, i, i+1)
            # result = max([result, word1, word2], key=lambda x: len(x))
            '''#instead of below if else statements use lamda function, 
            key is the keyword means that we find max in length '''
            if len(word1) >= len(word2):
                longest = word1
            else:
                longest = word2

            if len(longest) >= len(result):
                result = longest
            else:
                result = result
        return result




