def quicksort(arr):
    iter = 0
    qshelper(arr, 0, len(arr) - 1, iter)
    return arr

def qshelper(arr, start, end, iter):
    if start > end:
        return

    pivot = start
    left = start+1
    right = end

    while right >= left:
        if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
            arr[left], arr[right] = arr[right], arr[left] #swap

        elif arr[left] <= arr[pivot]:
            left = left+1

        elif arr[right] >= arr[pivot]:
            right = right-1

    arr[pivot], arr[right] = arr[right], arr[pivot]
    iter = iter + 1
    print(arr, iter)
    qshelper(arr, start, right -1,iter) # the first half gets sorted
    qshelper(arr, right+1, end,iter) # the second half gets sorted

quicksort([4,6,1,5,3,7,2])


