__author__ = "streethacker"

#!/usr/bin/python
#-*- coding:utf-8 -*-

# Data Structures and Algorithms Using Python
# CHAPTER 8: Queues
# Listing 8.1: pylistqueue.py


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

    def __init__(self):
        self._qList = list()

    def isEmpty(self):
        return len(self._qList) == 0

    def __len__(self):
        return len(self._qList)

    def __iter__(self):
        return _QueueIterator(self._qList)

    def __contains__(self, item):
        return item in self._qList

    def enqueue(self, item):
        self._qList.append(item)

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        return self._qList.pop(0)

    def printQueue(self):
        for item in self:
            print item

if __name__ == "__main__":
    Q = Queue()
    Q.enqueue(28)
    Q.enqueue(19)
    Q.enqueue(45)
    Q.enqueue(13)
    Q.enqueue(7)

    Q.printQueue()
