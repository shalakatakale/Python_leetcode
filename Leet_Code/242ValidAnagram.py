# 242 Valid Anagram
# O(n) complexity Hash Map
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        s_hash = {}
        for letter in s:
            if letter in s_hash:
                s_hash[letter] += 1
            else:
                s_hash[letter] = 1

        s_hash_zero = {}
        for letter in s:
            if letter in s_hash_zero:
                s_hash_zero[letter] = 0
            else:
                s_hash_zero[letter] = 0

        for letter in t:
            if letter in s_hash:
                s_hash[letter] -= 1

        if s_hash != s_hash_zero:
            return False
        else:
            return True
# O(nlog(n))
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s1 = sorted(s)
        t1 = sorted(t)
        if s1 == t1:
            return True

        return False

