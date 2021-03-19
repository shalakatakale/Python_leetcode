'''#9 Palindrome number
!!! don't use string work with int (number)
-121 is not palindrome as 121- is not same as -121
Also note that 10,20... etc will give palindrome when you try checking 1st half
with reverse of second half. therefore take those conditions
'''
class Solution(object):
    def isPalindrome(self, x):
        if x >= 2 ** 31 or x < 0:
            return False
        elif x % 10 == 0 and x != 0: # 0 is palindrome
            return False
        else:
            reverse_last_half = 0
            while reverse_last_half < x:
                reverse_last_half = reverse_last_half * 10 + x % 10
                x = x // 10

            return x == reverse_last_half or x == reverse_last_half // 10
        # x == reverse_last_half for 1221
        # x == reverse_last_half // 10 for 121

# Below solution is slower because it will check for entire number
class Solution(object):
    def isPalindrome(self, x):
        if x < -2 ** 31 or x >= 2 ** 31 or x < 0:
            return 0
        else:
            y = x
            reverse_x = 0
            while y:
                remainder = y % 10
                y = y // 10
                reverse_x = reverse_x * 10 + remainder
            return reverse_x == x


