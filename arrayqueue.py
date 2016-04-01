#!/usr/bin/python
#-*- coding:utf-8 -*-

# Data Structures and Algorithms Using Python
# CHAPTER 8: Queues
# Listing 8.2: arrayqueue.py

from array1d import Array


class _QueueIterator:

    def __init__(self, queue):
        self._queue = queue
        self._curItem = 0

    def __iter__(self):
        return self

    def next(self):
        if self._curItem < len(self._queue):
            item = self._queue[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration


class Queue:

    def __init__(self, maxSize):
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = Array(maxSize)

    def isEmpty(self):
        return self._count == 0

    def isFull(self):
        return self._count == len(self._qArray)

    def __len__(self):
        return self._count

    def __iter__(self):
        return _QueueIterator(self._qArray)

    def __contains__(self, item):
        return item in self._qArray

    def enqueue(self, item):
        assert not self.isFull(), "Cannot enqueue to a full queue."

        maxSize = len(self._qArray)
        self._back = (self._back + 1) % maxSize
        self._qArray[self._back] = item
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."

        item = self._qArray[self._front]
        self._front = (self._front + 1) % maxSize
        self._count -= 1
        return item

    def printQueue(self):
        for item in self:
            print item

if __name__ == "__main__":
    Q = Queue(8)
    Q.enqueue(28)
    Q.enqueue(19)
    Q.enqueue(45)
    Q.enqueue(13)
    Q.enqueue(7)

    Q.printQueue()
