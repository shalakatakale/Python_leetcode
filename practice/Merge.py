def mergesort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr)//2
    left = arr[0:middle]
    right = arr[middle:len(arr)]

    left_result = mergesort(left)
    right_result = mergesort(right)
    print("a", left_result)
    print("b", right_result)
    l = len(left_result)

    # return left_result
    # return right_result
    sortedarr = [None]*(len(left_result)+len(right_result))
    return sortedarr
print(mergesort([2,5,6,7,1,9,0]),'final answer')