'''#27 Remove Element
made a location array to store locations of val
because when you pop the length of original array will decrease by 1 each time
 so for example if you pop 2 times you have location in original nums + 2
 therefore you will have to make a -2'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        location = []
        for i in range(len(nums)):
            if nums[i] == val:
                location.append(i)
        for i in range(len(location)):
            a = location[i] - i
            nums.pop(a)
        return len(nums)

# Below solution is really cool
class Solution:
    def removeElement(self, nums, val):
        head = 0
        tail = len(nums) - 1

        if not nums: return 0

        while head <= tail:
            if nums[head] == val:
                nums[head] = nums[tail]
                tail -= 1
                continue

            head += 1
        return head