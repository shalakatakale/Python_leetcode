'''Difference between this and #1 two sum is that input array is sorted,
but solution of #1 works with Hash table works for this'''

# 1 two pointer
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
# 2 hash map
class Solution():
    def twoSum(self, nums, target):
        """
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
                """
        store = {} # this dictionary contains complement value of numbers in nums
        for i in range(len(nums)):  # O(n)
            if nums[i] in store: #  or write store.keys()
                return (store[nums[i]]+1, i+1)
            else:
                store[target - nums[i]] = i
                #append key as complement of nums[i] and value as index of nums


# 3 binary search
class Solution(object):
   def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1