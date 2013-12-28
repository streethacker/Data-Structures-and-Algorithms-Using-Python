__author__ = "streethacker"

#/usr/bin/python
#-*- coding:utf-8 -*-

#Data Structures and Alogtithms Using Python
#CHAPTER 7: Stacks
#Listing 7.x: extopostfix.py(a help module for postfixCal.py)

from lliststack import Stack

__metaclass__ = type

class ExtoPostfix:
	def __init__(self):
		self._isp = {'#':0, '(':1, '*':5, '/':5, '+':3, '-':3, ')':6}
		self._icp = {'#':0, '(':6, '*':4, '/':4, '+':2, '-':2, ')':1}
		self._postfix = []
		self._oprtStack = Stack()

	def __str__(self):
		self._postfix = [elem for elem in self._postfix if elem != ')' and elem != '(']
		return ','.join(self._postfix)

	def _getPostfix(self,expr):
		expr = expr.split()
		self._oprtStack.push('#')
		ch = expr.pop(0)
		while self._oprtStack.isEmpty()==False and ch != '#':
				if ch.isdigit():
						self._postfix.append(ch)
						ch = expr.pop(0)
				else:
						ch1 = self._oprtStack.peek()
						if self._isp[ch1] < self._icp[ch]:
								self._oprtStack.push(ch)
								ch = expr.pop(0)
						elif self._isp[ch1] > self._icp[ch]:
								out = self._oprtStack.pop()
								self._postfix.append(out)
						else:
								out = self._oprtStack.pop()

		for i in range(len(self._oprtStack)):
				ch1 = self._oprtStack.pop()
				self._postfix.append(ch1)

	def backExpr(self,expr):
		self._getPostfix(expr)
		self._postfix = [elem for elem in self._postfix if elem != ')' and elem != '(' and elem != '#']
		return self._postfix


if __name__ == "__main__":
		ex = ExtoPostfix()

		expr = raw_input()

		print ex.backExpr(expr)
