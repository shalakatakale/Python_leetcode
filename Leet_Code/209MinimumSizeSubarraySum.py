# 1 brute force
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if target <= nums[i]:
                return 1

        for length in range(2, len(nums) + 1):
            for i in range(len(nums)):
                sum_nums = sum(nums[i:length + i])
                if target <= sum_nums:
                    return length
        return 0
# 2 I think the complexity is O(nlog(n))
class Solution():
    def minSubArrayLen(self, target, nums):
        total = left = right = 0
        # res is the window
        res = len(nums)+1
        # res = math.inf
        while right < len(nums):
            total += nums[right]
            while total >= target:
                res = min(res, right-left+1) #this will keep only minimum window
                                            # and help during returning minimum
                total -= nums[left] # see if removing left element still keeps total >= target
                                    # such that we get smallest window
                left += 1     # now that you have removed left from total shift window ahead
            right += 1  # if total < target then include an element in right
        return res if res <= len(nums) else 0

# 3 O(n), but i think it is O(nlog(n))
    # this is same as above solution but we understand windows better becaue of the variable names
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        windowSum, windowStart = 0, 0
        minLength = math.inf
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            while windowSum >= s:
                minLength = min(minLength, windowEnd - windowStart + 1)
                windowSum -= nums[windowStart]
                windowStart += 1
        if minLength == math.inf:
            return 0
        return minLength


#4
def minSubArrayLen(self, s, nums):

    l = len(nums)
    sum = 0
    i = 0
    j = 0
    res = l + 1
    while sum < s:
        sum += nums[j]
        j += 1
        while sum >= s:
            if j - i < res:
                res = j - i
            sum -= nums[i]
            i += 1
        if j == l:
            break
    if res > l:
        return 0
    return res


