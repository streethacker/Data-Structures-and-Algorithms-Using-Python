__author__ = "streethacker"

#/usr/bin/python
#-*- coding:utf-8 -*-

#Data Structures and Algorithms Using Python
#CHAPTER 7: Stacks
#Listing 7.3: validatingCpp.py

from lliststack import Stack

def isValidSource(srcFile):
	"""
	The function accepts a file object, which we assume was previously opened and contains C++
	source code.The file is scanned one line at a time and each line is scanned one character
	at a time to determine if it contains properly paired and balanced delimiters.
	"""
	s = Stack()
	for line in srcFile:
			for token in line:
					if token in "{[(":
							s.push(token) #if token is one of the opening delimiters it should be pushed into the stack.
					elif token in ")]}":  #if token is one of the closing delimiters it should be checke by the following steps.
							if s.isEmpty():
									return False
							else:
									left = s.pop()
									if token == "}" and left != "{" or \
											token == "]" and left != "[" or \
												token == ")" and left != "(":
												return False
	return s.isEmpty()

if __name__ == "__main__":
		with open("/home/streethacker/maxMsub/maxMsub.cpp", "r") as srcFile:
				if isValidSource(srcFile):
						print "This is a valid C++ file."
				else:
						print "This is an invalid C++ file, cause delimiters are not balanced."
