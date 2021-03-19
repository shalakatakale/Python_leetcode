'''Given a string, find the first non-repeating character in
it and return its index. If it doesn't exist, return -1.
Complexity Analysis

Time complexity : O(N) since we go through the string of length N two times.
Space complexity : O(1) because English alphabet contains 26 letters.
'''
# note easier way of making dictionary
# dictionary = collections.counter(s)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        dictionary = {}
        for character in s:
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1

        # go char by char to find if a character has value 1 in dictionary
        for i, character in enumerate(s):
            if dictionary[character] == 1:
                return i
        return -1
''' Explaination: Ordered Dict will save the characters it encounters in 
same sequence as the original string. Hence it becomes easy to catch hold of the first
unique character. Then according to the counter variable, whenever the first 1 is encountered
the corresponding dict.key's index is returned from the original String.'''
# 2   import OrderedDict, Counter
from collections import OrderedDict, Counter
class Solution():
    def firstUniqChar(self, s: str) -> int:
        for i,j in OrderedDict(Counter(s)).items():
            if j == 1:
                return s.index(i)
        return -1

# 3
class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set()
        for i in range(len(s)):
            if s[i] not in visited:
                visited.add(s[i])
                if s.count(s[i]) == 1:
                    return i
        return -1