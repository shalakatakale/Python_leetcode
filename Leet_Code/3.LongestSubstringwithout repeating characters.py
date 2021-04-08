class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        seen = {}  # dictionary
        output = [1] * len(s)  # count will be stored at each index of s
        seen[s[0]] = 1  # put first char of s in seen
        count = 1  #count as 1 because 1st string is non repeating
        for i in range(len(s) - 1):  # note to check i till 2nd last as i+1 is there
            if s[i + 1] != s[i]:
                if s[i + 1] in seen:  # eg. abcdb - b != d but check if we saw it previously
                    for x in range(i + 1 - count,
                                   i):  # i+1-count will give the index where our non repeating subtring started
                        if s[x] == s[i + 1]:
                            count = i - x
                count += 1  # add i+1 char
                output[i + 1] = count
                if s[i + 1] not in seen:
                    seen[s[i + 1]] = 1

            elif s[i + 1] == s[i]:
                count = 1
                output[i + 1] = 1

        return max(output)


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0

        seen = {}  # Hash Map
        # output = [1]*len(s)
        seen[s[0]] = 1  # put first char of s in seen
        count = 1
        result = 1

        for i in range(len(s) - 1):
            if s[i + 1] == s[i]:
                count = 1
                # output[i+1] = 1
                result = max(result, count)

            elif s[i + 1] != s[i]:
                if s[i + 1] not in seen:
                    seen[s[i + 1]] = 1
                elif s[i + 1] in seen:
                    for x in range(i + 1 - count, i):
                        if s[x] == s[i + 1]:
                            count = i - x
                count += 1
                # output[i+1] = count
                result = max(result, count)

        # return max(output)
        return result

# Leeetcode solution Sliding Window and Hash Table
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res

# Better Sliding window and Hash map - Optimized Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans