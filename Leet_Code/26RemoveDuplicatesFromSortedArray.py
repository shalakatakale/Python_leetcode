'''#26 Remove duplicate from sorted array'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i <= len(nums) - 2:
            if nums[i + 1] == nums[i]:
                nums.pop(i)
            else:
                i = i + 1
        return len(nums)

