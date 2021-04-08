
# this is brute force by me  -not accepted by leetcode
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        n = len(T)
        output = []
        # output = [0]*n and then you can remove j>=n
        for i in range(n):
            j = i + 1
            while j < n:
                if T[j] > T[i]:
                    # output[i] = j-i
                    output.append(j - i)
                    break
                else:
                    j += 1

            if j >= n:
                output.append(0)

        return output

# Stack
# https://www.youtube.com/watch?v=uFso48YRRao watch to understand below
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(T)
        output = [0] * n
        for i, t in enumerate(T):

            while len(stack) > 0 and t > stack[-1][0]:
                _, j = stack.pop()
                output[j] = i - j

            stack.append((t, i))

        return output

# leetcode
class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = [] #indexes from hottest to coldest
        for i in xrange(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans