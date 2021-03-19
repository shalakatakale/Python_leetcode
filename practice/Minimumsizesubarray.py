
nums = [2,3,1,2,4,3]
s = 7
total = left = right = 0
res = len(nums) + 1
while right < len(nums):
    total += nums[right]
    print("total",total)
    while total >= s:
        res = min(res, right-left+1)
        total -= nums[left]
        print(total)
        left += 1
    right += 1