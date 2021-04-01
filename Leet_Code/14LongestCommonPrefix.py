'''14 Longest common Prefix'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs == [] or "" in strs:
            return ""
        else:
            shortest = strs[0]
            for s in strs:
                if len(s) < len(shortest):
                    shortest = s  # select shortest word in the list

            same = []
            for letter in shortest:
                same.append(letter)  # list of letters in shortest word

            for s in strs:
                if len(same) >= len(s):
                    min = len(s)
                else:
                    min = len(same)
                for i in range(0, min):
                    if same[i] != s[i]:
                        del same[
                            i:]  # since we want prefix to be same, we del all letters if letter at i is not the same
                        break
        return "".join(same)