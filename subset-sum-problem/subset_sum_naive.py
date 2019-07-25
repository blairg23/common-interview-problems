"""
Solves a basic subset sum problem using a naive approach.

The subset sum problem is this:

Given a list X and index i, is there a nonempty subset of X_1,...,X_i which sums to S?

This naive approach will only find integer pairs within X that sum to S.
"""

import random

if __name__ == '__main__':
    N = number_of_integers = 23
    max_integer = 10
    min_integer = -10
    S = requested_sum = 0
    X = list_of_integers = [random.randint(min_integer, max_integer) for i in range(N)]

    print(X)

    integer_pairs = []

    for integer_x in range(N):
        for integer_y in range(N):
            if integer_x != integer_y:
                list_of_integers_x = X[integer_x]
                list_of_integers_y = X[integer_y]
                if (list_of_integers_x + list_of_integers_y) == requested_sum:
                    integer_pairs.append((list_of_integers_x, list_of_integers_y))

    print(integer_pairs)
