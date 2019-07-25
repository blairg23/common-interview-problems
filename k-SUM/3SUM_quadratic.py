"""
From https://en.wikipedia.org/wiki/3SUM

This solves the 3SUM problem using the Quadratic algorithm.

The 3SUM problem asks if a given set of N real numbers contains three elements that sum to zero.

Solves in O(n^2).
"""

import random

if __name__ == '__main__':
    N = 123  # number of integers
    min_integer = -10
    max_integer = 10
    S = [random.randint(min_integer, max_integer) for i in range(N)]  # list of random integers from min_integer to max_integer
    integer_triples = set()

    print('---------------------------------------')

    print(f'List of N={N} random integers, S, where {min_integer} <= S_i <= {max_integer}: {S}')

    S = sorted(S)

    for i in range(0, N-2):
        a = S[i]
        start = i + 1
        end = N - 1
        while start < end:
            b = S[start]
            c = S[end]
            if a + b + c == 0:
                integer_triples.add(str(sorted([a, b, c])))
                # Continue search for all triplet combinations summing to zero.
                # We need to update both end and start together since the array values are distinct.
                start += 1
                end -= 1
            elif a + b + c > 0:
                end -= 1
            else:
                start += 1

    print(f'Unique triples of integers adding up to zero: {integer_triples}')