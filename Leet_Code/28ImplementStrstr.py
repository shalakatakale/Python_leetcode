'''#28 implement str str'''
# don't use this solution in interview because it directly uses in-built functions
class Solution(object):
    def strStr(self, haystack, needle):

        if needle==None:
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1

# don't use this solution in interview because it directly uses in-built functions
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1

# Sliding Window - Use this solution O((n-L)*n) complexity
        L, n = len(needle), len(haystack)
        if L== 0:
            return 0
        pn = 0
        while pn < n-L+1:
            while pn < n-L+1 and haystack[pn] != needle[0]:
                pn += 1

            current_len = pl = 0
            while pl< L and pn<n and haystack[pn]== needle[pl]:
                pn += 1
                pl += 1
                current_len += 1

            if current_len == L:
                return pn-L
            else: # backtrack
                pn = pn-current_len+1
        return -1



# See leetcode to understand below rabin karp solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        if L > n:
            return -1

        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2 ** 31

        # lambda-function to convert character to integer
        h_to_int = lambda i: ord(haystack[i]) - ord('a')
        needle_to_int = lambda i: ord(needle[i]) - ord('a')

        # compute the hash of strings haystack[:L], needle[:L]
        h = ref_h = 0
        for i in range(L):
            h = (h * a + h_to_int(i)) % modulus
            ref_h = (ref_h * a + needle_to_int(i)) % modulus
        if h == ref_h:
            return 0

        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
            if h == ref_h:
                return start

        return -1