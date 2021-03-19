class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index = len(nums1) - len(nums2)
        for i in range(len(nums2)):
            nums1[index + i] = nums2[i]
        for iter in range(len(nums1)):
            for i in range(0, len(nums1) - 1 - iter):
                if nums1[i] > nums1[i + 1]:
                    nums1[i], nums1[i + 1] = nums1[i + 1], nums1[i]
        return nums1

# Not accepted below
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        index = len(nums1) - len(nums2)
        for i in range(len(nums2)):
            nums1[index + i] = nums2[i]
        for i in range(len(nums2)):
            for j in range(len(nums2)):
                if nums1[i] >= nums1[index + j]:
                    nums1[i], nums1[index + j] = nums1[index + j], nums1[i]
                elif nums1[i] < nums1[index + j]:
                    nums1[index + j], nums1[i] = nums1[index + j], nums1[i]
        return nums1
