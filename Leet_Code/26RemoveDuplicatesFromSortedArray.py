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

        # two pointer solution faster than above
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return len(nums[0:i + 1])

