'''263. Ugly Number also remember 1 is treated as ugly number'''
# 1
class Solution(object):
    def isUgly(self, num):
        for p in 2, 3, 5:
            while num % p == 0 < num:
            # while num % p == 0 and num: this is what the above line means
                num /= p
        return num == 1
# 2
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while num!=1:
            if num%2 == 0:
                num = num/2
            elif num%3 == 0:
                num = num/3
            elif num%5 == 0:
                num = num/5
            else:
                return False
        return True

# this is what I came up with but it doesn't work
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        primes = []
        i = 2
        while i < num:
            if num % i == 0:
                primes.append(i)
                num = num / i
            else:
                i = i + 1

        if 2 in primes or 3 in primes or 5 in primes:
            while primes:
                primes.remove(2)
                primes.remove(3)
                primes.remove(5)

            if len(primes) > 0:
                return False
            else:
                return True
        else:
            return False
