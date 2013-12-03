__author__ = "streethacker"

#/usr/bin/python
#-*-coding:utf-8-*-

#Data Structures and Algorithms Using Python
#CHAPTER 3: Sets and Maps
#Listing 3.2: linearmap.py

class _MapEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value

class _MapIterator:
	def __init__(self, theMap):
		self._mapRef = theMap
		self._curNdx = 0

	def __iter__(self):
		return self

	def next(self):
		if self._curNdx < len(self._mapRef):
				item = self._mapRef[self._curNdx]
				self._curNdx += 1
				return item
		else:
				raise StopIteration


class Map:
	def __init__(self):
		self._entryList = list()

	def __len__(self):
		return len(self._entryList)

	def __contains__(self, key):
		ndx = self._findPosition(key)
		return ndx is not None

	def __getitem__(self, key):
		ndx = self._findPosition(key)
		assert ndx is not None, "Invalid map key."
		return self._entryList[ndx].value

	def __setitem__(self, key, value):
		ndx = self._findPosition(key)
		if ndx is not None:
				self._entryList[ndx].value = value
				return False
		else:
				entry = _MapEntry(key, value)
				self._entryList.append(entry)
				return True

	def remove(self, key):
		ndx = self._findPosition(key)
		assert ndx is not None, "Invalid map key."
		self._entryList.pop(ndx)

	def __iter__(self):
		return _MapIterator(self._entryList)

	def _findPosition(self, key):
		for i in range(len(self)):
				if self._entryList[i].key == key:
						return i
		else:
				return None


if __name__ == "__main__":
		m = Map()
		m["ID"] = 1001
		m["NAME"] = "Jhon Smith"
		m["AGE"] = 22

		print m["ID"]
		print m["NAME"]
		print m["AGE"]

