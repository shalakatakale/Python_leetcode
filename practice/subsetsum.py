nums = [1,2,3,4]
target = 7

#def SubsetSum(nums, target):
    # dp matrix from row 0 to len of array
    # col 0 t0 target
t = [[None] * (target + 1) for _ in range(len(nums) + 1)]
    # intialization
for i in range(len(nums) + 1):
    for j in range(target + 1):
        # below is row 0 is target is given but no element in array
        if i == 0:
            t[i][j] = False
        # below is col 0, elements are available but target is 0, So you
        # can always choose subset of 0 elements, So True
        if j == 0:
            t[i][j] = True

for i in range(len(nums) + 1):
    for j in range(target + 1):
        if nums[i - 1] <= j:
            t[i][j] = t[i-1][j-nums[i-1]] or t[i-1][j]

        else:
            t[i][j] = t[i-1][j]
    value =  t[len(nums)][target]
print(value)
print(t)