'''204 Count Primes, Could not think on my own'''
#  Sieve of Eratosthenes Python
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True for i in range(n+1)]
        p = 2
        while p*p<=n:
            if prime[p]:
                for i in range(p*p,n+1,p):
                    prime[i]=False
            p+=1
        res = []
        for p in range(2,n):
            if prime[p]:
                res.append(p)
        return len(res)



# Brute Force, time exceeds from 499979
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        listofprime = []
        if n > 1:
            for i in range(2, n):
                for j in range(2,int(i/2) +1) :
                    if i%j == 0:
                        break
                else:
                    listofprime.append(i)
            return len(listofprime)
        else:
            return 0
