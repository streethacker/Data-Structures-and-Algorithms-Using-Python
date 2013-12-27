__author__ = "streethacker"

#/usr/bin/python
#-*- coding:utf-8 -*-

from lliststack import Stack

__metaclass__ = type

class ExtoPostfix:
	def __init__(self):
		self._isp = {'#':0, '(':1, '*':5, '/':5, '+':3, '-':3, ')':6}
		self._icp = {'#':0, '(':6, '*':4, '/':4, '+':2, '-':2, ')':1}
		self._postfix = []
		self._oprtStack = Stack()

	def __str__(self):
		return ','.join(self._postfix)

	def postfix(self,expr):
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


if __name__ == "__main__":
		ex = ExtoPostfix()

		expr = raw_input()

		ex.postfix(expr)

		print ex
