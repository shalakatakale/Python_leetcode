''' 416 Partition equal subset sum
See subsetsum.py
Given a non-empty array nums containing only positive integers,
find if the array can be partitioned into two subsets such that
the sum of elements in both subsets is equal. '''
# DP solution below from youtube DP series
# O(n*m)
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_nums = sum(nums)
        target = sum_nums // 2
        if sum_nums % 2 != 0:
            return False

        elif sum_nums % 2 == 0:
            return self.SubsetSum(nums, target)

    def SubsetSum(self, nums, target):
        t = [[None] * (target + 1) for _ in range(len(nums) + 1)]

        # intialization
        for i in range(len(nums) + 1):
            for j in range(target + 1):
                if i == 0:
                    t[i][j] = False
                if j == 0:
                    t[i][j] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    t[i][j] = t[i - 1][j - nums[i - 1]] or t[i - 1][j]

                else:
                    t[i][j] = t[i - 1][j]
        return t[len(nums)][target]

# Brute Force - Recursion


# O(m*n)

class Solution:
    def canPartition(self, nums):
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2

        # construct a dp table of size (subset_sum + 1)
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]

        return dp[subset_sum]
