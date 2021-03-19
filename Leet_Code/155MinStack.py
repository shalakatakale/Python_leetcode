'''155 create a stack and get minimum value in a stack. Also perform push, pop, top (peek) operations'''

class MinStack():
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, x):
        self.stack.append(x)

        if self.minstack:
            if x <= self.minstack[-1]:
                self.minstack.append(x)
        else:
            self.minstack.append(x)

    def pop(self):
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getmin(self):
        return self.minstack[-1]

my_stack = MinStack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(5)
my_stack.push(8)
print(my_stack.getmin())
print(my_stack.top())
my_stack.pop()
my_stack.push(3)
print(my_stack.getmin())

