'''#53 Maximum subarray
This was too tricky for me'''
class Solution:
    def maxSubArray(self, nums):
        max_end = 0
        max_sofar = -9876543   #Any random neative (large number)

        for i in nums:
            max_end += i

            if max_end > max_sofar:
                max_sofar = max_end

            if max_end < 0:
                max_end = 0

        return max_sofar