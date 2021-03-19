# 49 Group Anagram
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

# Solution complexity N*K*log(K)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        element_sorted = []
        for strings in strs:
            element_sorted.append(''.join(sorted(strings)))
            # complexity N*K*log(K) for above 
        index_hash = {}
        for i, element in enumerate(element_sorted):
            if element in index_hash:
                index_hash[element].append(strs[i])
            else:
                index_hash[element] = [strs[i]]

        return index_hash.values()
# COmplexity N*K
class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()