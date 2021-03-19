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
