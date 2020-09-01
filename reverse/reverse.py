from queue import Queue


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        container = Queue()
        while node:
            container.enqueue(node.value)
        while container.size != 0:
            llist = LinkedList()
            if self.head is None:
                value = container.dequeue()
                self.head = Node(value)
                llist.add_to_head(self.head)
            elif self.head.get_next() is None:
                value = container.dequeue()
                node = Node(value)
                llist.add_to_head(node)
                self.head.set_next(node)
                node = prev
            else:
                value = container.dequeue()
                node = Node(value)
                llist.add_to_head(node)
                prev.set_next(node)
                node = prev
