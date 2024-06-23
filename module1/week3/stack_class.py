class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.num_list = []

    def is_empty(self):
        if len(self.num_list) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.num_list) == self.capacity:
            return True
        else:
            return False

    def push(self, value):
        return self.num_list.append(value)

    def pop(self):
        return self.num_list.pop(-1)

    def top(self):
        return self.num_list[-1]


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)

print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
