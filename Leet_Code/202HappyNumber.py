'''#202 Happy Number
My solution because I did not know that number that eventually sums to 4 is unhappy
so I used count such that the while loop will stop. It got accepted'''
'''Like stated above you will not know that the number that ends up to 4 is never going to be happy number 
So use Hashtable to see if a number was obtained before '''


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = {}
        while n > 0:
            sum1 = sum([(int(x) ** 2) for x in str(n)])
            # digit = [int(x) for x in str(n)]
            # sum1 = 0
            # for i in digit:
            # sum1 += i*i
            ''' # instead of str and int 
                       sum1 = 0
                       while n > 0:
                           n, digit = divmod(n, 10)
                           # digit = n%10
                           # n = n/10
                           sum1 += digit**2
            '''
            if sum1 == 1:
                return True

            elif sum1 in seen:
                return False

            elif sum1 not in seen:
                seen[sum1] = 1
                # seen.add(n) if you use seen = set() instead of seen = {}

            n = sum1

        return False

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        count = 10
        while n > 0 and count > 0:
            digit = [int(x) for x in str(n)]
            sum1 = 0
            for i in digit:
                sum1 += i * i

            if sum1 == 1:
                return True
            n = sum1
            count -= 1
        return False
#  Floyd's Cycle-Finding Algorithm from leetcode solutions
def isHappy(self, n: int) -> bool:
    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    slow_runner = n
    fast_runner = get_next(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_next(slow_runner) # slow runner goes one step ahead at a time
        fast_runner = get_next(get_next(fast_runner)) # note that fast runner goes two steps ahead at a time
    return fast_runner == 1

# below solution is with sum == 4, No count
# this is hardcoding - so don't use in interviews
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n > 0:
            digit = [int(x) for x in str(n)]
            sum1 = 0
            for i in digit:
                sum1 += i * i

            if sum1 == 1:
                return True
            elif sum1 == 4:
                return False
            n = sum1

        return False # okay even if this return False not there



