class IndexedQueue:
    def __init__(self):
        self.queue = list()
        self.__queue_size = 0
        self.start_index = 0

    def size(self):
        return self.__queue_size

    def add(self, item):
        self.queue.append(item)
        self.__queue_size += 1

    def pop_first(self):
        if self.__queue_size == 0:
            return None

        if self.start_index == self.__queue_size - 1:
            return None
        else:
            first_item = self.queue[self.start_index]
            self.__queue_size -= 1
            self.start_index += 1
            return first_item


def test():
    q = IndexedQueue()
    assert (q.pop_first() is None)
    q.add(1)
    q.add(2)
    assert (q.pop_first() == 1)
    assert (q.pop_first() == 2)
    assert (q.pop_first() is None)
    assert (q.size() == 0)

