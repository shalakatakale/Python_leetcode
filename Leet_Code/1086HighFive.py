'''1086 High Five'''


class Solution(object):
    def highFive(self, items):
        id_score = {}
        result = []
        items.sort(reverse=True)

        for x in items:
            if x[0] in id_score:
                id_score[x[0]].append(x[1])
            else:
                id_score[x[0]] = [x[1]]

        for ids, score in id_score.items():
            total = 0
            i = 0
            while i < 5 and i < len(score):
                total += score[i]
                i += 1
            result.append([ids, total // i])
        return result

# 2
for ids, score in id_score.items():
    total = sum(id_score[ids][:5])

    result.append([ids, total // 5])
return result

'''for i in range(len(items)):

    if items[i][0] in id_score:
       # append doesn't work here
       # error : 'int' object has no attribute 'append'
       # but it will work with 1086 high five solution
            id_score[items[i][0]].append(items[i][1])
    else:               #id not in dict
        id_score[items[i][0]] = items[i][1]
print(id_score)'''