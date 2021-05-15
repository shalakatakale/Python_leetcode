# 561 Array Position
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        # using sorting
        # O(n*log(n))
        # eg.[6,2,6,5,1,2] after sort is [1,2,2,5,6,6]
        # min among pairs is the even index element
        nums.sort()
        sum_even = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                sum_even += nums[i]

        return sum_even

        # one line solution
        # return sum(j for i,j in enumerate(sorted(nums)) if i%2==0)
        # return sum(sorted(nums)[::2])

        # O(n)
        class Solution(object):
            def arrayPairSum(self, nums):

                res = [0] * 20001

        for x in nums:
            res[x + 10000] += 1
        s_so_far, adjust = 0, False
        for idx, freq in enumerate(res):
            if freq:
                freq = freq - 1 if adjust else freq
                if freq & 1:
                    s_so_far += ((freq // 2) + 1) * (idx - 10000)
                    adjust = True
                else:
                    s_so_far += ((freq // 2)) * (idx - 10000)
                    adjust = False
        return s_so_far
