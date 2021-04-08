from collections import OrderedDict


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        seen = OrderedDict()
        left = right = 0
        max_len = 1

        while right < n:
            seen[s[right]] = right
            right += 1

            if len(seen) == 3:
                del_index = min(seen.values())
                del seen[s[del_index]]
                left = del_index + 1

            max_len = max(max_len, right - left)
        return max_len

# Instead of maintaining a hashmap, using set to find out distinct characters.
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        longest = [0, 0]
        occ = {}
        idx = 0
        for index, el in enumerate(s):
            if len(set(s[idx:index + 1])) <= 2:
                if longest[1] - longest[0] < (index - idx + 1):
                    longest = [idx, index + 1]
            else:
                idx += 1

        return longest[1] - longest[0]

#
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if len(s) <= 2:
            return len(s)
        d = dict() #store the visited char and the frequency
        start, end = 0, 0 #two pointers
        count = 0
        res = 1
        while start < len(s): #we loop the string once with start
            while end < len(s) and count <= 2: #we loop the string once with end, overall
                if s[end] not in d:
                    d[s[end]] = 1
                    count += 1 #increase the counter
                else:
                    d[s[end]] += 1
                end += 1
            res = max(res, end - start) if count <= 2 else max(res, end-start-1) #update the max length
            d[s[start]] -= 1
            if d[s[start]] == 0:
                del d[s[start]]
                count -= 1 #decrease the counter when moving start pointer
            start += 1
        return res
