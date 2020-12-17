"""
define a single function, `fib(n)`, that returns the nth Fibonacci number.
The first 10 terms of the Fibonacci sequence are
`[0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...]`
Make sure that your `fib(n)` function correctly handles values of n <= 0.
If you choose to implement `fib(n)` as a recursive function,
your code will have problems if it does not handle values of n <= 0.
 """
# https://www.geeksforgeeks.org/python-program-for-n-th-fibonacci-number/

# !/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(n):
    '''returns the nth Fibonacci number '''
    if n <= 0:
        return n
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
