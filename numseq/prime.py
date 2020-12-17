# !/usr/bin/env python
# -*- coding: utf-8 -*-

def primes(n):
    '''Returns a list of all prime numbers less than n '''
    list = []
    for num in range(1, n + 1):
        if is_prime(num):
            list.append(num)
    return list


def is_prime(m):
    '''Returns a boolean indicating whether `m` is a prime number '''
    if m <= 1:
        return False
    elif m == 2:
        return True
    else:
        for num in range(2, m):
            if m % num == 0:
                return False
        return True
