class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # hashmap 1
        hash_nums = {}
        result = []
        for num in nums:
            hash_nums[num] = 1

        for num in range(1, len(nums) + 1):
            if num not in hash_nums:
                result.append(num)

        return result

        arr = [0] * len(nums)
        output = []
        for i in range(len(nums)):
            arr[nums[i] - 1] = nums[i]

        for i in range(len(arr)):
            if arr[i] == 0:
                output.append(i + 1)
        return output

        # hashmap 2
        arr = [n for n in range(1, len(nums) + 1)]
        hash_arr = collections.Counter(arr)
        for i in range(len(nums)):
            if nums[i] in hash_arr:
                del hash_arr[nums[i]]

        output = hash_arr.keys()
        return output



