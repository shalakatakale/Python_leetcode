"""Arrange the array from lowest to highest value by swapping the smallest value
that is right of the value at current index  in the list with the value at current index.
Next change the current index by +1 and do the above step again.
Time Complexity is best - O(n**2); average - O(n**2); worst -  O(n**2); Space Complexity worst - O(1)"""

def selectionsort(my_array):                     # eg. my_array = [10,  8, 13, 5, 4]
    for i in range(len(my_array)):               #eg. len(my_array) = 5
        min_x = i                                # eg. i = 0
        for item in range(i+1, len(my_array)):   # then item in range(1,5)
            if my_array[item] < my_array[min_x]: # ie. my_array[1] < my_array[0] that's true
                min_x = item                     # then min_x = item = 1 ie. value 10 will be at index 1
        my_array[i], my_array[min_x] = my_array[min_x], my_array[i]  # swap 10 with 3
        print(i, my_array)

my_array  = [10, 8, 13, 5, 4]
selectionsort(my_array)
print("final answer", my_array)