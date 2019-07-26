"""
From https://en.wikipedia.org/wiki/3SUM

This solves the 3SUM problem using a simple hashtable lookup.

The 3SUM problem asks if a given set of N real numbers contains three elements that sum to zero.

Solves in O(n^2).
"""

import random


if __name__ == '__main__':
    N = 123  # number of integers
    min_integer = -10
    max_integer = 10
    S = [random.randint(min_integer, max_integer) for i in range(N)]  # list of random integers from min_integer to max_integer
    hashtable = {}
    integer_triples = set()  # Set to hold the unique triples of integers that sum to zero

    print('---------------------------------------')

    print(f'List of N={N} random integers, S, where {min_integer} <= S_i <= {max_integer}: {S}')

    for integer in S:
        hashtable[str(integer)] = 1

    for i in range(N):
        for j in range(N):
            if i != j:
                if str(-1 * (i + j)) in hashtable:
                    integer_triples.add(str(sorted([i, j, -1 * (i + j)])))

    print(f'Unique triples of integers adding up to zero: {integer_triples}')
