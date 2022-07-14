class LinkedListNode:
    def __init__(self, value):
        self.__value = value
        self.next_node = None

    def value(self):
        return self.__value

    def set_next(self, node):
        self.next_node = node

    def get_next(self):
        return self.next_node


class NullNode(LinkedListNode):
    def __init__(self):
        super().__init__(None)


class LinkedListQueue:
    def __init__(self):
        self.__queue_size = 0
        self.first_node = NullNode()
        self.last_node = NullNode()

    def size(self):
        return self.__queue_size

    def add(self, value):
        if self.__queue_size == 0:
            self.first_node = LinkedListNode(value)
            self.first_node.set_next(NullNode())
            self.last_node = self.first_node
        else:
            new_last_node = LinkedListNode(value)
            self.last_node.set_next(new_last_node)
            self.last_node = new_last_node
        self.__queue_size += 1

    def pop_first(self):
        if self.__queue_size == 0:
            return None
        else:
            first_value = self.first_node.value()
            self.first_node = self.first_node.get_next()
            self.__queue_size -= 1
            return first_value


def test():
    q = LinkedListQueue()
    assert (q.pop_first() is None)
    q.add(1)
    q.add(2)
    assert (q.pop_first() == 1)
    assert (q.pop_first() == 2)
    assert (q.pop_first() is None)
    assert (q.size() == 0)
