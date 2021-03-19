nums = [1,1,4,2,1,3]
nums2 = sorted(nums)
print(nums2)



strs = ["eat","tea","tan","ate","nat","bat"]
element_sorted = []
for strings in strs:
    element_sorted.append(''.join(sorted(strings)))
print(element_sorted)

index_hash = {}
for i, element in enumerate(element_sorted):

    if element in index_hash:
        index_hash[element].append(strs[i])
    else:
        index_hash[element] = [strs[i]]

print(index_hash)


