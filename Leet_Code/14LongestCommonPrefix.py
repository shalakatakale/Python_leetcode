'''14 Longest common Prefix'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs == [] or "" in strs:
            return ""
        else:
            prefix = strs[0]
            same = []
            for s in strs:
                if len(s) < len(prefix):
                    prefix = s
            for letter in prefix:
                same.append(letter)
            for s in strs:
                if len(same)>=len(s):
                    min = len(s)
                else:
                    min = len(same)
                for i in range(0, min):
                    if same[i] != s[i]:
                        del same[i:]
                        break
        return "".join(same)


