'''#20 Valid Parenthesis
Use Stack, map, stack.pop()'''
class Solution(object):
    def isValid(self, s):
        if int(len(s) % 2)!= 0:
            return False
        else:
            map_1 = {'(': ')', '[': ']', '{': '}'}
            open_brac = ['(','[','{']
            stack = []
            for i in s:
                if i in open_brac:
                    stack.append(i)
                elif stack and i==map_1[stack[-1]]:
                    stack.pop()
                else:
                    return False
            return stack == []

# more time complexity because of while
class Solution(object):
    def isValid(self, s):
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''

#
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '{', '[']
        right = [')', '}', ']']
        stack = []
        for letter in s:
            if letter in left:
                stack.append(letter)
            elif letter in right:
                if len(stack) <= 0:
                    return False
                if left.index(stack.pop()) != right.index(letter):
                    return False
        return len(stack) == 0
