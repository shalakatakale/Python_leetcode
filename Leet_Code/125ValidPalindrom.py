# 125 Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # way 1
        # a = "".join([c.lower() for c in s if c.isalnum()])

        # way 2
        b = "" # b = [] would be wrong cause it is string not array
        for element in s:
            if element.isalnum():
                b += "".join(element) # don't you forget the + that is to add
        a = b.lower()

        # way 1 for finding if palindrome
        # if a == a[::-1]:
            #return True
        # return False

        # way 2
        left , right = 0 ,  len(a) - 1
        while left <= right and left >= 0 and right < len(a):
            if a[left] != a[right]:
                return False
            elif a[left] == a[right]:
                left += 1
                right -= 1
        return True

# 2
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True
