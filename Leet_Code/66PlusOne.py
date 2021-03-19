'''#66 Plus One '''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = []
        for i in digits:
            number.append(str(i))
        number = "".join(number)
        number = int(number) + 1
        new_2 = str(number)
        # new_1 = new_2.split()
        return list(new_2)
# 2
def plusOne(self, digits):
    return list(str(int(''.join([str(i) for i in digits]))+1))

# 3 RECURSION
class Solution:
    def plusOne(self, digits):
        def add_one(index):
            if index < 0:
                digits.insert(0, 1)
                return

            digits[index] = (digits[index] + 1) % 10

            if not digits[index]:
                add_one(index - 1)

        add_one(len(digits) - 1)

        return digits

