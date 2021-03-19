"""my_array is sorted in ascending
   for element not in the array return -1
   Binary Search complexity = O(log(n))"""

def binarysearch(my_array, target):
    left = 0
    right = len(my_array)-1

    while left <= right:
        middle = (left+right)//2
        middle_element = my_array[middle]

        if target == middle_element:
            return middle
        elif target < middle_element:
            right = middle-1
        elif target > middle_element:
            left = middle+1
    return -1

print(binarysearch([1,2,3,4,5,6,7,8,9],6))


