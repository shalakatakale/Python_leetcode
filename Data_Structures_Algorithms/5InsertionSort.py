"""Insertion sort - there is a sorted list and an unsorted list. eg. [10, 20, 5, 12, 7];
we first consider 10 as sorted list (last = i -1 ; at starting 1-1 = 0; arr[0] = 10.
20 will be key = arr[i]. 20 is greater than 10, therefore skip while loop and
arr[last +1] = arr[1-1+1] = arr[1] = key = 20).
Now i = 2; key =  arr[2] = 5; last = 1; key(5) < arr[last = 1], so arr[last + 1 = 2] = arr[last = 1];
last = last -1 = 0; again since it is while loop, key(5) < arr[last = 0](10).
therefore now arr[last +1 = 1] = arr[0] = 10. arr[last +1] = 5......an so on
Time Complexity is best - O(n); average - O(n**2); worst -  O(n**2); Space Complexity worst - O(1)"""

def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        last = i - 1
        while last >= 0 and key < arr[last]:
            arr[last + 1] = arr[last]
            last = last - 1
        arr[last + 1] = key
        print(i, arr)

arr = [10, 20, 5, 12, 7]
insertionsort(arr)
print(arr)
