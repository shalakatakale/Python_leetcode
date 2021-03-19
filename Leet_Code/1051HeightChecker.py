# 1051 Height checker
# complexity may be O(nlog(n)) because sorted would need that
# although for has O(n)
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        nums_sorted = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != nums_sorted[i]:
                count += 1

        return count

# 2 O(n)
from collections import Counter
class Solution:
    def heightChecker(self, heights):
        counter = Counter(heights)

        i = 0

        removals = 0
        for height in heights:
            while counter[i] == 0:
                i += 1

            if i != height:
                removals += 1

            counter[i] -= 1

        return removals

# 3
class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        max_val = max(heights)

        # Create frequency table
        freq = [0] * (max_val + 1)
        for num in heights: freq[num] += 1
        for num in range(1, len(freq)): freq[num] += freq[num - 1]

        # Create places table
        places = [0] * len(heights)
        for num in heights:
            places[freq[num] - 1] = num
            freq[num] -= 1

        return sum([a != b for a, b in zip(heights, places)])