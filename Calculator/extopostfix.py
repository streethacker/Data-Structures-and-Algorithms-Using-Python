__author__ = "streethacker"

#/usr/bin/python
#-*- coding:utf-8 -*-

# Data Structures and Alogtithms Using Python
# CHAPTER 7: Stacks
# Listing 7.x: extopostfix.py(a help module for postfixCal.py)

from lliststack import Stack

__metaclass__ = type


class ExtoPostfix:
    """
    Receive an infix expression and turn it into a postfix expression.
    This is a helper module of postfixCal.py.
    """

    def __init__(self):
        self._isp = {
            '#': 0,
            '(': 1,
            '*': 5,
            '/': 5,
            '+': 3,
            '-': 3,
            ')': 6}  # in stack priority
        self._icp = {
            '#': 0,
            '(': 6,
            '*': 4,
            '/': 4,
            '+': 2,
            '-': 2,
            ')': 1}  # in coming priority
        # the list used to save the final postfix expression.
        self._postfix = []
        # the stack used to change the order of operators.
        self._oprtStack = Stack()

    def __str__(self):
        self._postfix = [
            elem for elem in self._postfix if elem != ')' and elem != '(']
        return ','.join(self._postfix)

    def _getPostfix(self, expr):
        """
        Algorithm:
        1)initialize the _oprtStack by pushing '#' into it.
        2)read in the first element of the infix expr, and assign it to variable ch.
        3)repeat the following steps until ch = '#', meanwhile, the top element of the _oprtStack is also '#':
                a)if ch is operand, append it to the _postfix, and read the next ch;
                b)if ch is operator, compare the priority(icp) of ch and the priority(isp) of the top element(op) in  _oprtStack:
                        if icp(ch) > isp(op), push ch onto _oprtStack, and read another ch
                        if icp(ch) < isp(op), pop the top element in _oprtStack, and append it to _postfix
                        if icp(ch) == isp(op), pop the top element in _oprtStack,if op is '(', read another ch.
        """
        expr = expr.split()
        self._oprtStack.push('#')
        ch = expr.pop(0)
        while self._oprtStack.isEmpty() == False and ch != '#':
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
                    if out == '(':
                        ch = expr.pop(0)

        for i in range(len(self._oprtStack) - 1):
            ch1 = self._oprtStack.pop()
            self._postfix.append(ch1)

    def backExpr(self, expr):
        self._getPostfix(expr)
        return self._postfix


if __name__ == "__main__":
    ex = ExtoPostfix()

    expr = raw_input()

    print ex.backExpr(expr)
