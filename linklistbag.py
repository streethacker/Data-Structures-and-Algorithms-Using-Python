__author__ = "streethacker"

#/usr/bin/python
#-*- coding:utf-8 -*-

# Data Structures and Algorithms Using Python
# CHAPTER 6: Linked Structures
# Listing 6.5: linklistbag.py


class _BagIterator:

    def __init__(self, theHead):
        self._curNode = theHead

    def __iter__(self):
        return self

    def next(self):
        """
        It's important to check the empty or null reference situation first.
        Because None object has no attribute 'next'. It will cause an  excep
        -tion.
        """
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.data
            self._curNode = self._curNode.next
            return item


class _BagListNode:
    """
    Defines a private storage class for creating list nodes. There are
    only two attributes: data field and next reference field.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class Bag:

    def __init__(self):
        """
        The self._size field is used to keep track of the number of items
        stored in the bag that is needed by the __len__ method. Technical
        -ly, this field is not needed. But it does prevent us from having
        to traverse the list to count the number of nodes each time the l
        -ength is needed.
        """
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        return _BagIterator(self._head)

    def __contains__(self, target):
        """
        The contains() method is a simle search of the linked list.
        """
        curNode = self._head
        while curNode is not None and curNode.data != target:
            curNode = curNode.next
        return curNode is not None

    def add(self, data):
        """
        The add() method simply implements the prepend operation, though
        we must also increment the item counter(_size) as new items are
        added.
        """
        newNode = _BagListNode(data)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    def remove(self, data):
        """
        The remove operation of the bag has a precondition that the item
        must be in the bag in order to be removed. If we make it pass the
        assertion, the item counter is decremented to reflect one less it
        -em in the bag, the node containing the item is unlinked from the
        linked list, and the item is returned as required by the ADT.
        """
        preNode = None
        curNode = self._head

        while curNode is not None and curNode.data != data:
            preNode = curNode
            curNode = curNode.next

        assert curNode is not None, "The item must be in the bag."

        self._size -= 1
        if curNode is self._head:
            self._head = curNode.next
        else:
            preNode.next = curNode.next

        return curNode.data

    #	try:
    #			if curNode is self._head:
    #					self._head = curNode.next
    #			else:
    #					preNode.next = curNode.next
    #			return curNode.data
    #	except AttributeError, e:
    #			print "The item must be in the bag."
    #			print e
    #	else:
    #			self._size -= 1
    #			return curNode.data

    def printBagElements(self):
        for b in self:
            print b


if __name__ == "__main__":
    bag = Bag()

    bag.add(10)
    bag.add(12)
    bag.add(36)
    bag.add(77)

    bag.printBagElements()

    bag.remove(12)

    print

    bag.printBagElements()
