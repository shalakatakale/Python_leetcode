'''#202 Happy Number
My solution because I did not know that number that eventually sums to 4 is unhappy
so I used count such that the while loop will stop. It got accepted'''

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

# below solution is with sum == 4, No count
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



