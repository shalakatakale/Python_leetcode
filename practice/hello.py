input = "Hello, World"
ls = (chr for chr in input if chr.isalpha())
print(ls)


# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = []

vowels = dict.fromkeys(keys, value)
print(vowels)

value.append(2)
print(vowels)

# note that all values for all keys will get updated here
vowels['o'] += [5]
print(vowels['o'])
print(vowels)

dict_1 = {'s': [1], 't':[1]}
dict_1['s'] += [5]
print(dict_1['s'])
print(dict_1)

inorder = [9,3,15,20,7]
print(enumerate(inorder))

memory = {}
for i, e in enumerate(inorder):
    memory[e] = i

# below is memory[3] idx is value of the key 3
idx =memory.get(3)

print(idx)
print(memory)



