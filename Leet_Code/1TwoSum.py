'''1. Two Sum - Array, Hash table (dictionary) '''
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
                return (store[nums[i]], i) , print(store)
            else:
                store[target - nums[i]] = i
                #append key as complement of nums[i] and value as index of nums


## Example Execution ##
obj = Solution()
result = obj.twoSum([2,4,757,6,43,15,1,1,11,12], 8)
print(result)

# 2 faster
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        visited = {}

        for i in range(len(nums)):

            if target - nums[i] in visited:
                return [i, visited[target - nums[i]]]

            visited[nums[i]] = i





