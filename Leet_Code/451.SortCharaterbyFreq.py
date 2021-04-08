'''451 Sort Character by Freq '''
class Solution(object):
    def frequencySort(self, s):
        dict2 = {}
        for x in s:
            if x not in dict2:
                dict2[x] = 1
            else:
                dict2[x] += 1

        a = sorted(dict2.items(), key=lambda x: x[1], reverse= True )
        output = []
        for letter, number in a:
            output.append(letter*number)

        out = "".join(output)
        return out
# This is good too
# see leetcode
def frequencySort(self, s: str) -> str:
    if not s: return s

    # Determine the frequency of each character.
    counts = collections.Counter(s)
    max_freq = max(counts.values())

    # Bucket sort the characters by frequency.
    buckets = [[] for _ in range(max_freq + 1)]
    for c, i in counts.items():
        buckets[i].append(c)

    # Build up the string.
    string_builder = []
    for i in range(len(buckets) - 1, 0, -1):
        for c in buckets[i]:
            string_builder.append(c * i)

    return "".join(string_builder)

# below solution has O(n**2) complexity and hence not accepted in leetcode
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict1 = collections.Counter(s)
        print(dict1)
        new = [None] * len(s)
        s1 = []
        for char in s:
            s1.append(char)

        for j in range(len(s1) - 1):
            for i in range(len(s1) - 1):
                if dict1[s1[i]] < dict1[s1[i + 1]]:
                    s1[i], s1[i + 1] = s1[i + 1], s1[i]
                elif dict1[s1[i]] == dict1[s1[i + 1]]:
                    if ord(s1[i]) < ord(s1[i + 1]):
                        s1[i], s1[i + 1] = s1[i + 1], s1[i]
                else:
                    pass

        return "".join(s1)

# below is leetcode solutions but it uses inbuilt functions
def frequencySort(self, s: str) -> str:
    # Count up the occurances.
    counts = collections.Counter(s)

    # Build up the string builder.
    string_builder = []
    for letter, freq in counts.most_common():
        # letter * freq makes freq copies of letter.
        # e.g. "a" * 4 -> "aaaa"
        string_builder.append(letter * freq)
    return "".join(string_builder)