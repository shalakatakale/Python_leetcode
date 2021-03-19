def mergesort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr)//2
    left = arr[0:middle]
    right = arr[middle:len(arr)]

    left_result = mergesort(left)
    right_result = mergesort(right)

    return merge(left_result, right_result)

def merge(left_result, right_result):
    sortedarr = [None]*(len(left_result)+len(right_result)) #create empty sorted arr
    i = j = k = 0
    while i < len(left_result) and j < len(right_result):
        if left_result[i] <= right_result[j]:
            sortedarr[k] = left_result[i]
            i += 1
        else:
            sortedarr[k] = right_result[j]
            j +=1
        k +=1
    while i < len(left_result):
        sortedarr[k] = left_result[i]
        i += 1
        k +=1

    while j < len(right_result):
        sortedarr[k] = right_result[j]
        j += 1
        k +=1

    return sortedarr

print(mergesort([2,5,6,7,1,9,0,3]),'final answer')



