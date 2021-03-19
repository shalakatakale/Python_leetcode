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