from collections import defaultdict
seq = [2,2,3,2,3]

# use any of the below two lines to create dictionary
#tally = defaultdict(list)
tally = {}
for i, num in enumerate(seq):
    if num not in tally:
        tally[num] = [i]
    elif num in tally:
        tally[num].append(i)

print(tally)

# get unique values in a list
nums = [1,2,3,1,2,3]
nums_unique_set = set(nums)
print(nums_unique_set)
nums_unique_list = list(nums_unique_set)
print(nums_unique_list)

#  zip
# The zip() function takes iterables (can be zero or more),
# aggregates them in a tuple, and return it.
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
result = zip(coordinate, value)
print(result)
result_list = list(result)
print(result_list)
c, v =  zip(*result_list)
print('c =', c)
print('v =', v)


numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

# converting to list
result_list2 = list(result)
print(result_list2)





