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

    def enqueue(self, value):
        return self.num_list.append(value)

    def dequeue(self):
        return self.num_list.pop(0)

    def front(self):
        return self.num_list[0]


stack1 = MyStack(capacity=5)
stack1.enqueue(1)
stack1.enqueue(2)

print(stack1.is_full())
print(stack1.front())
print(stack1.dequeue())
print(stack1.front())
print(stack1.dequeue())
print(stack1.is_empty())
