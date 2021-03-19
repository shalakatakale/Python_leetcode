'''217 Contains Duplicate -  Hash Map will take O(n) complexity
or sorting will take O(nlogn) complexity
Very Easy'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = 1

        return False
