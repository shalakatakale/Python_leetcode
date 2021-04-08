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

# method 4 best complexity is given for  pointer approach O(n+m)
class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]
        p1 = 0
        p2 = 0
        for p in range(n + m):
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1


# this one gives best runtime O(n+m)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        while n > 0:
            nums1[n - 1] = nums2[n - 1]
            n -= 1

        return nums1

# below is using merge sort - O(log(n))
# but it doesn't work on leetcode because they want nums1 as result
# the changes should be made in nums1
class Solution(object):
    def merge(self, nums1, m, nums2, n):

        index = len(nums1) - len(nums2)
        nums1 = nums1[0:index]
        print(nums1)
        result = []
        index_left = index_right = 0
        while len(result) < len(nums1) + len(nums2):
            if nums1[index_left] <= nums2[index_right]:
                result.append(nums1[index_left])
                index_left += 1
            else:
                result.append(nums2[index_right])
                index_right += 1

            if index_right == len(nums2):
                result += nums1[index_left:]
                break

            if index_left == len(nums1):
                result += nums2[index_right:]
                break
        print(result)
        return result



# Not accepted below because too much complexity
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



