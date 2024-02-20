#    Main Author(s): 
#    Main Reviewer(s):



class Stack:
    def __init__(self, cap=10):
        self.capacity_value = cap
        self.stack_list = []

    def capacity(self):
        return self.capacity_value

    def push(self, data):
        self.stack_list.append(data)
        if len(self.stack_list) > self.capacity_value:
            self.capacity_value *= 2

    def pop(self):
        if self.is_empty():
            raise IndexError('pop() used on empty stack')
        return self.stack_list.pop()

    def get_top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def is_empty(self):
        return len(self.stack_list) == 0

    def __len__(self):
        return len(self.stack_list)


class Queue:
    def __init__(self, cap=10):
        self.capacity_value = cap
        self.queue_list = []

    def capacity(self):
        return self.capacity_value

    def enqueue(self, data):
        self.queue_list.append(data)
        if len(self.queue_list) > self.capacity_value:
            self.capacity_value *= 2

    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue() used on empty queue')
        return self.queue_list.pop(0)

    def get_front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def is_empty(self):
        return len(self.queue_list) == 0

    def __len__(self):
        return len(self.queue_list)


class Deque:
    def __init__(self, cap=10):
        self.capacity_value = cap
        self.deque_list = []

    def capacity(self):
        return self.capacity_value

    def push_front(self, data):
        self.deque_list.insert(0, data)
        if len(self.deque_list) > self.capacity_value:
            self.capacity_value *= 2

    def pop_front(self):
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')
        return self.deque_list.pop(0)

    def push_back(self, data):
        self.deque_list.append(data)
        if len(self.deque_list) > self.capacity_value:
            self.capacity_value *= 2

    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
        return self.deque_list.pop()

    def get_front(self):
        if self.is_empty():
            return None
        return self.deque_list[0]

    def get_back(self):
        if self.is_empty():
            return None
        return self.deque_list[-1]

    def is_empty(self):
        return len(self.deque_list) == 0

    def __len__(self):
        return len(self.deque_list)

    def __getitem__(self, k):
        if 0 <= k < len(self.deque_list):
            return self.deque_list[k]
        else:
            raise IndexError('Index out of range')

# Example usage:
# stack = Stack()
# queue = Queue()
# deque = Deque()
