'''#13 Roman to Integer '''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        normal_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        special_map = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        list = []
        number = 0
        for i in range(len(s)-1):
            if s[i]+s[i+1] in special_map.keys():
                number = number + special_map[s[i]+s[i+1]]
                list.append(i)
                list.append(i+1)
        for j in range(len(s)):
            if j not in list:
                number = number + normal_map[s[j]]
        return number

'''#13 Roman to Integer '''
class Solution(object):
    def romanToInt(self, s):
        values = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000,"IV": 4,"IX": 9,"XL": 40, "XC": 90,"CD": 400,"CM": 900}
        total = 0
        i = 0
        while i < len(s):
            # This is the subtractive case.
            if i<len(s)-1 and s[i:i+2] in values:
                total += values[s[i:i+2]]
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total
#
class Solution:
    def romanToInt(self, s):
        values = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}

        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += values[s[i]]
                i += 1
        return total

#
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        res = mapping[s[0]]
        for i in range(1, len(s)):
            res += mapping[s[i]]
            if mapping[s[i - 1]] < mapping[s[i]]:
                res -= 2 * mapping[s[i - 1]]

        return res