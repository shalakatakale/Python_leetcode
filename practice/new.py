
nums = [1,5,11,6]
target = 11

t= [[None] * (target + 1) for _ in range(len(nums) + 1)]
for i in range(len(nums) + 1):
    for j in range(target + 1):
        if i == 0:
            t[i][j] = False
        if j == 0:
            t[i][j] = True

'''for j in range(target + 1):
    if nums[0] <= j:
        t[1][j] = True
    else:
        t[1][j] = False'''

print(t)


class_name_labele = {class_name : i for i,class_name in enumerate(nums)}
print(class_name_labele)

