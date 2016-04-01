__author__ = "streethacker"

#/usr/bin/python
#-*- coding:utf-8 -*-

# Data Structures and Algorithms Using Python
# CHAPTER 5: Searching and Sorting
# Listing 5.10: binaryset.py

from linearset import Set


class binarySet(Set):
    """
    Improvement of the linearset by using the binary search and
    merge lists on sorted lists. Inherited from the linearset.

    Comparison of the two Set ADT implementations:
    +---------------------------------------------------+
    s = Set()/binarySet()		O(1)		O(1)
    len(s)						O(1)		O(1)
    x in s						O(n)		O(logn)
    s.add(x)					O(n)		O(n)
    s.isSubsetOf(t)				O(n^2)		O(n)
    s == t						O(n^2)		O(n)
    s.union(t)					O(n^2)		O(n)
    +---------------------------------------------------+
    """

    def __contains__(self, element):
        ndx = self._findPosition(element)
        return ndx < len(self) and self._theElements[ndx] == element

    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            for i in range(len(self)):
                if self._theElements[i] != setB._theElements[i]:
                    return False
            return True

    def add(self, element):
        if element not in self:
            ndx = self._findPosition(element)
            self._theElements.insert(ndx, element)

    def remove(self, element):
        assert element in self, "The element must be in the set."
        ndx = self._findPosition(element)
        self._theElements.pop(ndx)

    def isSubsetOf(self, setB):
        if len(self) > len(setB):
            return False
        else:
            for i in range(len(self)):
                if self._theElements[i] != setB._theElements[i]:
                    return False
            return True

    def union(self, setB):
        newSet = binarySet()
        a = b = 0

        while a < len(self) and b < len(setB):
            valueA = self._theElements[a]
            valueB = self._theElements[b]

            if valueA < valueB:
                newSet._theElements.append(valueA)
                a += 1
            elif valueA > valueB:
                newSet._theElements.append(valueB)
                b += 1
            else:
                newSet._theElements.append(valueA)
                a += 1
                b += 1

        while a < len(self):
            newSet._theElements.append(self._theElements[a])
            a += 1

        while b < len(setB):
            newSet._theElements.append(setB._theElements[b])
            b += 1

        return newSet

    def _findPosition(self, element):
        low, high = 0, len(self._theElements) - 1

        while low <= high:
            mid = (low + high) / 2

            if self._theElements[mid] == element:
                return mid
            elif element < self._theElements[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return low


if __name__ == "__main__":
    smith = binarySet()
    smith.add("CSCI-112")
    smith.add("MATH-121")
    smith.add("HIST-340")
    smith.add("ECON-101")

    roberts = binarySet()
    roberts.add("POL-101")
    roberts.add("ANTH-230")
    roberts.add("CSCI-112")
    roberts.add("ECON-101")

    if smith == roberts:
        print "Smith and Roberts are taking the same courses."
    else:
        sameCourses = smith.intersection(roberts)
        if sameCourses.isEmpty():
            print "Smith and Roberts are not taking any of the same courses."
        else:
            print "Smith and Roberts are taking some of the same courses:"
            for course in sameCourses:
                print course

    print "All the courses they take:"
    for course in smith.union(roberts):
        print course
