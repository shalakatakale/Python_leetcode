# 724. Find Pivot Index
# complexity O(n)
# Space Complexity: O(1) to store leftsum
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == sum(nums) - leftsum - x:
                return i
            leftsum += x
        return -1

# Same as above but explained using weighing balance scale
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # Initialization:
        # Left hand side be empty, and
        # Right hand side holds all weights.
        total_weight_on_left, total_weight_on_right = 0, sum(nums)

        for idx, current_weight in enumerate(nums):

            total_weight_on_right -= current_weight

            if total_weight_on_left == total_weight_on_right:
                # balance is met on both sides
                # i.e., sum( nums[ :idx] ) == sum( nums[idx+1: ] )
                return idx

            total_weight_on_left += current_weight

        return -1
