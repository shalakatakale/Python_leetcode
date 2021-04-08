import collections

s = 'treeeeeqqq'

dict1 = collections.Counter(s)
print(dict1)


dict2 = {}
for x in s:
    if x not in dict2:
        dict2[x] = 1
    else:
        dict2[x] += 1

print(dict2)

a = sorted(dict2.items(), key=lambda x: x[1], reverse= True )
print("a", a)

output = []
for letter, number in a:
    output.append(letter*number)

print("".join(output))
