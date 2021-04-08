from collections import OrderedDict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        n = len(s)
        if n == 0 or k == 0:
            return 0

        seen = OrderedDict()  # dictionary
        left = right = 0
        max_length = 1
        while right < n:
            seen[s[right]] = right
            right += 1

            if len(seen) == k + 1:
                del_index = min(seen.values())
                del seen[s[del_index]]
                left = del_index + 1

            max_length = max(max_length, right - left)
        return max_length

# leetcode solution
from collections import OrderedDict


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        n = len(s)
        if n == 0 or k == 0:
            return 0

        seen = OrderedDict()  # dictionary
        left = right = 0
        max_length = 1

        while right < n:
            character = s[right]
            if character in seen:
                del seen[character]

            seen[character] = right
            right += 1

            if len(seen) == k + 1:
                _, del_index = seen.popitem(last=False)
                left = del_index + 1

            max_length = max(max_length, right - left)
        return max_length