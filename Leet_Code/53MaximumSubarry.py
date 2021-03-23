'''#53 Maximum subarray'''
# Approach 1: Divide and Conquer
# time O(nLog(n))
# space O(log(n)) because of its recursion stack
# leetcode solution
'''Define the base case(s).
Split the problem into sub problems and solve them recursively.
Merge the solutions for the sub problems to obtain the solution for the original problem.'''
class Solution:
    def cross_sum(self, nums, left, right, p):
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p, left - 1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(p + 1,
                       right + 1):  # right = len(nums) -1 ie index of right, so to                                         include last element take right+1
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]

        p = (left + right) // 2

        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)

        return max(left_sum, right_sum, cross_sum)

    def maxSubArray(self, nums):
        return self.helper(nums, 0, len(nums) - 1)

# 2. Greedy
# Pick the locally optimal move at each step,
# and that will lead to the globally optimal solution.
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum

# Approach 3: Dynamic Programming (Kadane's algorithm)
# Time O(n)
# space O(1)
# There are two standard DP approaches suitable for arrays:
# Constant space one. Move along the array and modify the array itself.
# (Fixed Sliding window)Linear space one. First move in the direction left->right,
# then in the direction right->left. Combine the results.
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)

        return max_sum

# This was too tricky for me
class Solution:
    def maxSubArray(self, nums):
        max_end = 0
        max_sofar = -9876543 # use float('-inf') instead of this random number
                             #Any random negative (large number)
        for i in nums:
            max_end += i

            if max_end > max_sofar:
                max_sofar = max_end

            if max_end < 0:
                max_end = 0

        return max_sofar