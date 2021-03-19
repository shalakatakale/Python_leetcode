'''#35 search insert position'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head = 0
        tail = len(nums)-1
        while head <= tail:
            index = (head + tail) //2
            if target > nums[index]:
                head = index + 1
            elif target < nums[index]:
                tail = index - 1
            elif target == nums[index]:
                return index
        return head

# one line code below
class Solution:
    def searchInsert(self, nums, target):
        return sorted(nums + [target]).index(target)

# use index, append, sort or sorted 
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for x in range(len(nums)):
            if target in nums:
                return nums.index(target)
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)