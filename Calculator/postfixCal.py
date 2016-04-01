__author__ = "streethacker"

#/usr/bin/python
#-*- coding:utf-8 -*-

# Data Structures and Algorithms Using Python
# CHAPTER 7
# Listing 7.x

from lliststack import Stack
from extopostfix import ExtoPostfix
import sys

__metaclass__ = type


class Calculator:
    """
    A simple calculator which process a postfix expr and return the result of the arithmetic expr.
    """

    def __init__(self, expr):
        # _expr is a list, which contains the split of the expr.
        self._expr = []
        # _stack is a stack, whick is a main structure in the processing.
        self._stack = Stack()

        # split the expr string into a list, which turn operands into floats
        # and remain the operators              #as string.
        for elem in expr:
            if elem not in ['+', '-', '*', '/']:
                self._expr.append(float(elem))
            else:
                self._expr.append(elem)

    def _calResult(self):
        """
        _calResult is the main process routine which calculate the result of the expr:
        1.If the current item is an operand, push its value onto the stack.
        2.If the current item is an operator:
                a)Pop the top two operands off the stack.
                b)Perform the operation.(Note the top value is the right operand while the next to the top value is the left operand.
                c)Push the reuslt of the operation back onto the stack.

        Invalid Exprs:
                a)More operands than operators:
                If the stack is empty, we can stop the evaluation and flag an error.
                b)More operators than operands:
                If the stack is not empty(at the end), the expression was invalid and we must flag an error.
                Actually, we can check the size of the stack when all the elements in _expr is used.If it equals 1, the expr is valid,
                otherwise invalid.
        """
        for elem in self._expr:
            if elem not in ['+', '-', '*', '/']:
                self._stack.push(elem)
            else:
                try:
                    roprd = self._stack.pop()
                    loprd = self._stack.pop()
                    if elem == '+':
                        self._stack.push(loprd + roprd)
                    elif elem == '-':
                        self._stack.push(loprd - roprd)
                    elif elem == '*':
                        self._stack.push(loprd * roprd)
                    else:
                        self._stack.push(loprd / roprd)
                # AssertionError indicates the _stack is already empty, expr
                # invalid.
                except AssertionError as AssErr:
                    print "The expression you input is wrong(too many operators). Please check it again."
                    print "Error Message:", AssErr.message if AssErr.message else "None"
                    sys.exit()
                # used for division operators, zero can not be used as an
                # divident.
                except ZeroDivisionError as DivErr:
                    print "Zero can not used as an divident."
                    print "Error Message:", DivErr.message if DivErr.message else "None"
                    sys.exit()
                except Exception as ExcErr:  # catch the unexpected exceptions.
                    print "Unknown Error."
                    print "Error Message", ExcErr.message if ExcErr.message else "None"
                    sys.exit()

        try:
            # at the end of the for loop, check the size of _stack, if equals
            # 1, valid, otherwise invalid.
            if len(self._stack) != 1:
                raise AssertionError
            else:
                result = self._stack.pop()
                return result
        except AssertionError as AssErr:
            print "The expression you input is wrong(too many operands). Please check it again."
            print "Error Message:", AssErr.message if AssErr.message else "None"
            sys.exit()

    def backResult(self):
        """
        Format the result of the expr.
        """
        self._calResult()
        print "The result of the arithmetic is:%.2f" % self._calResult()

if __name__ == "__main__":
    expr = raw_input("please input the expression:")

    ex_parser = ExtoPostfix()

    expr = ex_parser.backExpr(expr)

    parser = Calculator(expr)

    parser.backResult()
