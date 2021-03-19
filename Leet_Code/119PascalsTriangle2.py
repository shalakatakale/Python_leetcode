'''#119 Pascals Triangle 2'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        output = [[1]*(i+1) for i in range(rowIndex+1)]
        for j in range(rowIndex+1):
            for i in range(1,j):
                output[j][i] = output[j-1][i-1] + output[j-1][i]
        return output[-1]

# below you don't make the output you only may elements in output
class Solution(object):
    def getRow(self, rowIndex):
        pascal =  [1]*(rowIndex + 1)
        # here you already made pascal for rowIndex 0 and 1
        for i in range(2,rowIndex+1): # start making pascal for rowIndex 2 and above
            for j in range(i-1,0,-1):
                pascal[j] += pascal[j-1]
        return pascal