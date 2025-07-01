class CircularQueue:
    DEFAULTY_CAPACITY = 10

    def __init__(self):

        self._data = [None] * CircularQueue.DEFAULTY_CAPACITY
        self._size = 0
        self._front = 0

    # def len(self):

    #     return self._size

    def is_Empty(self):
        return self._size == 0

    def first(self):
        if self.is_Empty():
            # raise exits the method(kinda like return)
            raise Empty("Queue is Empty")
        return self._data[self._front]

    def dequeue(self):
        if self.is_Empty():
            raise Empty("Queue is empty for dequeue operation")

        front = (self._front + 1) % len(self._data)

        dequeued_element = self._data[self._front]
        # garbage collection  -> assign it to none making it available for reuse
        self._data[self._front] = None
        self._size -= 1

        return dequeued_element

    def enqueue(self, data):
        # check if queue is full
        if self._size == len(self._data):
            # Increasing the size
            self._resize(2 * len(self._data))
        #     Computing the last position in queue
        tail = (self._front + self._size) % len(self._data)

        # insert new data and reassign to tail
        self._data[tail] = data
        self._size = self._size + 1

    def _resize(self, new_capacity):
        ...


class Empty(Exception):
    pass


if __name__ == "__main__":

    obj_q = CircularQueue()

    insert_el = [11, 22, 33, 44, 55]
    # print("\n Current Queue Representation:")
    for element in insert_el:
        obj_q.enqueue(element)

        print((f"Added Element:{element}"))
        print(f"New queue size:{obj_q._size}")