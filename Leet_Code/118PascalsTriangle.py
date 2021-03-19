'''#118 Pascals Triangle - Array '''
def generate(numRows):
    pascal = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal

# below by me
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # output = [0]*numRows
        output = []
        for j in range(1, numRows + 1):
            elements = [1] * j
            left = 0
            right = 1
            for i in range(1, j - 1):
                #elements[i] = output[j - 2][left] + output[j - 2][right]
                # write above instead below
                #elements[i] = output[j - 2][i - 1] + output[j - 2][i]
                # use above and instead of left write i-1 and instead of right write i
                element_prev = output[j - 2]
                elements[i] = element_prev[left] + element_prev[right]
                left += 1
                right += 1
            # output[j-1] = elements
            output.append(elements)
        return output
# See below to know how to use insert and extend
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        output = [[1],[1,1]]
        for i in range(3,numRows+1):
            last = output[-1]
            newlist =[]
            for i in range(len(last)-1):
                newlist.append(last[i]+last[i+1])
            newlist.insert(0,1)
            newlist.extend([1])
            output.append(newlist)
        return output
