"""
From https://en.wikipedia.org/wiki/Subset_sum_problem

Solves a basic subset sum problem using a naive approach.

The subset sum problem is this:

Given a list X and index i, is there a nonempty subset of X_1,...,X_i which sums to S?

This naive approach will only find integer pairs within X that sum to S.

Solves in O(n^2).
"""

import random

if __name__ == '__main__':
    N = 123  # number of integers
    min_integer = -10
    max_integer = 10
    S = 0  # initial sum to achieve
    X = [random.randint(min_integer, max_integer) for i in range(N)]  # list of random integers from min_integer to max_integer
    integer_pairs = set()  # Set to hold the unique pairs of integers that sum to zero

    print('---------------------------------------')

    print(f'List of N={N} random integers, X, where {min_integer} <= X_i <= {max_integer}: {X}\n')

    print(f'S={S}\n')

    for integer_x in range(N):
        for integer_y in range(N):
            if integer_x != integer_y:
                list_of_integers_x = X[integer_x]
                list_of_integers_y = X[integer_y]
                if (list_of_integers_x + list_of_integers_y) == S:
                    integer_pairs.add(tuple(sorted([list_of_integers_x, list_of_integers_y])))

    print(f'Unique pairs of integers adding up to S={S}: {integer_pairs}')
