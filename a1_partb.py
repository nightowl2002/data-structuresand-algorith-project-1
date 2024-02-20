#    Main Author(s): Jatin


class Node:
    def __init__(self, data=None, next_node=None, previous_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_previous(self):
        return self.previous_node


class SortedList:
    def __init__(self):
        self.front = None
        self.back = None

    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    def is_empty(self):
        return self.front is None

    def __len__(self):
        count = 0
        current = self.front
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def insert(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.back = new_node
        else:
            current = self.front
            previous = None
            while current is not None and data > current.get_data():
                previous = current
                current = current.get_next()

            if previous is None:
                # Insert at the beginning
                new_node.next_node = self.front
                self.front.previous_node = new_node
                self.front = new_node
            elif current is None:
                # Insert at the end
                new_node.previous_node = self.back
                self.back.next_node = new_node
                self.back = new_node
            else:
                # Insert in the middle
                new_node.next_node = current
                new_node.previous_node = previous
                previous.next_node = new_node
                current.previous_node = new_node

        return new_node

    def erase(self, node):
        if node is None:
            raise ValueError('Cannot erase node referred to by None')

        previous_node = node.get_previous()
        next_node = node.get_next()

        if previous_node is None:
            # Node is the front
            self.front = next_node
        else:
            previous_node.next_node = next_node

        if next_node is None:
            # Node is the back
            self.back = previous_node
        else:
            next_node.previous_node = previous_node

    def search(self, data):
        current = self.front
        while current is not None:
            if current.get_data() == data:
                return current
            elif current.get_data() > data:
                break
            current = current.get_next()

        return None
