

import collections
nums= [3,4,5,2,3,1]
count = collections.Counter(nums)
print(count)
print(sorted(count))

from collections import Counter
counter = Counter(nums)
print(counter)

nums= [-3,4,-5,2,3,1]
# new = nums - [9]*len(nums)
# print(abs(nums))

wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
new = []
store1 = []
store2 = []

for i in range(len(wordsDict)):
    if wordsDict[i] == word1:
        store1.append(i)
    if wordsDict[i] == word2:
        store2.append(i)

print(store1,store2)


