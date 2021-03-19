"""my_array is sorted in ascending
   for element not in the array return -1
   Binary Search Recursion complexity = O(log(n))"""

def binarysearchrecursion(my_array, target):
    left = 0
    right = len(my_array) - 1
    # Helper Function is going to do the recursive task
    result = helper(my_array, target, left, right)
    return result

def helper(my_array, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    middle_element = my_array[middle]

    if target == middle_element:
        return middle
    elif target < middle_element:
        right = middle - 1
        result = helper(my_array, target, left, right)
        return result
    elif target > middle_element:
        left = middle + 1
        result = helper(my_array, target, left, right)
        return result

print(binarysearchrecursion([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
