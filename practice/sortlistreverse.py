items =  [[1,90],[1,86],[2,87],[3,87],[1,89],[2,56],[3,45],[1,67],[3,23]]

items.sort(reverse = True)

print(items)

# items = items[7][0]
# print(items)

id_score = {}
for i in range(len(items)):

    if items[i][0] in id_score:
       # append doesn't work here
       # error : 'int' object has no attribute 'append'
       # but it will work with 1086 high five solution
            id_score[items[i][0]].append(items[i][1])
    else:               #id not in dict
        id_score[items[i][0]] = items[i][1]
print(id_score)