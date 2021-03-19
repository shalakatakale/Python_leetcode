"""Bubble sort compares 2 neighbouring elements in an array at a time to arrange all the
elements in ascending.
Time Complexity is best - O(n); average - O(n**2); worst -  O(n**2); Space Complexity worst - O(1)"""

def bubblesort(my_array):
    for iter in range(len(my_array)):
        for i in range(0, len(my_array) - 1 - iter):
            if my_array[i] > my_array[i+1]:
                my_array[i], my_array[i+1] = my_array[i+1], my_array[i]
                print("iter{} does {}".format(iter, my_array))
        print("iter{} is complete".format(iter))


my_array = [4,3,2,1,0]
bubblesort(my_array)
print(my_array)
