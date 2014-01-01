__author__ = "streethacker"

#!/usr/bin/python
#-*- coding:utf-8 -*-

#Data Structures and Algorithms Using Python
#CHAPTER 13: Binary Trees
#Listing 13.6/13.7/13.8/13.9: exptree.py

from collections import deque

class _ExpTreeNode:
	def __init__(self, data):
		self.element = data
		self.left = None
		self.right = None

class ExpressionTree:
	def __init__(self, expStr):
		self._expTree = None	#storing the reference of root node.
		self._buildTree(expStr)	#helper method:actually constructs the tree.

	def evaluate(self, varMap):
		return self._evalTree(self._expTree, varMap)	#helper method:evaluate the expr tree and returns the numeric result.

	def __str__(self):
		return self._buildString(self._expTree)	#helper method:recursively builds a string representation of the expr tree.

	def _buildString(self, treeNode):
		#if the node is a leaf, it's an operand.
		if treeNode.left is None and treeNode.right is None:
				return str(treeNode.element)
		else:	#otherwise, it's an operator.
				expStr = '('	#a left parenthesis needs to be printed before a subtree is visited.
				#an inOrder recursion:
				expStr += self._buildString(treeNode.left)
				expStr += str(treeNode.element)
				expStr += self._buildString(treeNode.right)
				expStr += ')'	#a right parenthesis needs to be printed after a subtree has been visited.
				return expStr

	def _evalTree(self, subtree, varDict):
		#if the node is a leaf node, return its value
		if subtree.left is None and subtree.right is None:
				assert subtree.element in varDict, "Invalid variable."
				return varDict[subtree.element]
		else:
		#otherwise, it's an operator that needs to be computed.
			#a postOrder recursion, whearas exchange the print function to _computeOp function
				lvalue = self._evalTree(subtree.left, varDict)
				rvalue = self._evalTree(subtree.right, varDict)
				return self._computeOp(lvalue, subtree.element, rvalue)

	def _computeOp(self, left, op, right):
		if op == '+':
				return float(left) + float(right)
		elif op == '-':
				return float(left) - float(right)
		elif op == '*':
				return float(left) * float(right)
		elif op == '/':
				assert float(right) != 0.0, "Devidient could not be zero."
				return float(left) / float(right)
		else:
				assert int(left) == float(left) and int(right) == float(right), "The two operands of % operator must be integers."
				return int(left) % int(right)

	def _buildTree(self, expStr):
		#build a queue containing the tokens in the expr string.
		expQ = deque()
		for token in expStr:
				expQ.append(token)

		#create an empty root node.
		self._expTree = _ExpTreeNode(None)
		self._recBuildTree(self._expTree, expQ)	#call the recursive function to build the expr tree.

	def _recBuildTree(self, curNode, expQ):
		token = expQ.popleft()	#extract the next token from the queue.

		#see if the token is a left parenthesis
			#the only times we descend down the tree is after encountering a left parenthesis or an operator
		if token == '(':
				curNode.left = _ExpTreeNode(None)
				self._recBuildTree(curNode.left, expQ)

				#the next token will be an operator:+ - / * %
				curNode.element = expQ.popleft()
				curNode.right = _ExpTreeNode(None)
				self._recBuildTree(curNode.right, expQ)

				expQ.popleft()	#the next token will be a right parenthesis, remove it.
		else:	#otherwise, the token is a digit
				curNode.element = token

if __name__ == "__main__":
		expStr = "((a*b)+c)"
		expr = ExpressionTree(expStr)

		print expr
		print expr.evaluate({'a':2, 'b':7, 'c':8})
