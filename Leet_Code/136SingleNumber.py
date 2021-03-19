class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        found = {}
        for i, num in enumerate(nums):
            if num in found:
                found[num] += 1
            else:
                found[num] = 1
        # below is simpler
        #for a in found:
        #    if found[a] == 1:
        #        return a
        key_list = list(found.keys())
        val_list = list(found.values())
        number = val_list.index(1)
        return key_list[number]

# 2
# Concept
# 2 * (a + b + c) - (a + a + b + b + c) = c2∗(a+b+c)−(a+a+b+b+c)=c
# set(nums) gives you distinct numbers in the list or tuple
class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

# 3 Keep taking xor
# a xor a  = 0
# 0 xor a = a
# eventually a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a