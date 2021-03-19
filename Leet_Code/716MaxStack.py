'''716 Max Stack - last pop max is important'''
# 1 with just 1 stack. here we use max
class MaxStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def peekMax(self):
        return max(self.stack)

    def popMax(self):
        self.stack = self.stack[::-1]
        maxnum = self.stack.pop(self.stack.index(max(self.stack)))
        self.stack = self.stack[::-1]

        return maxnum

#2 with 2 stacks. 1 is stack and 2 is max stack
class MaxStack(object):

    def __init__(self):
        self.stack = []
        self.maxstack = []

    def push(self, x):
        self.stack.append(x)
        if self.maxstack:
            if x >= self.maxstack[-1]:
                self.maxstack.append(x)
        else:
            self.maxstack.append(x)

    def pop(self):
        if self.maxstack[-1] == self.stack[-1]:
            self.maxstack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.maxstack[-1]

    def popMax(self):
        temp = []

        while self.stack[-1] != self.maxstack[-1]:
            temp.append(self.stack[-1])
            self.stack.pop()

        self.stack.pop()
        res = self.maxstack.pop()

        while temp:
            self.push(temp[-1])
            temp.pop()

        return res