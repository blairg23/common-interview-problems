"""
From https://en.wikipedia.org/wiki/Subset_sum_problem

Solves a basic subset sum problem using dynamic programming.

The subset sum problem is this:

Given a list X and index i, is there a nonempty subset of X_1,...,X_i which sums to S?

Solves in O(N(B - A))
where
A = sum of negative values in X
B = sum of positive values in X.
and
A <= S <= B
"""

import random


def Q(x, i, s):
    """
    :param list x: A random list of positive and negative integers.
    :param int i: A given index.
    :param int s: The chosen S value, oftentimes zero.
    :return bool: Given a list X, returns a boolean value if there is a nonempty subset of X_1,...,X_i which sums to S.
    """
    if i == 0:
        print(f'Q({i}, {s}) => Base Case: Checking if {x[i]} == {s}')
        if x[i] == s:
            print('Result: True')
            print('\n')
            return True
        else:
            print('Result: False')
            print('\n')
            return False

    print(f'Q({i}, {s}) => Checking if Q({i - 1}, {s}) or ({x[i]} == {s}) or Q({i - 1}, {s - x[i]})\n')
    if Q(x, i - 1, s) or (x[i] == s) or Q(x, i - 1, s - x[i]):
        print(f'Q({i}, {s}) => Checked if Q({i - 1}, {s}) or ({x[i]} == {s}) or Q({i - 1}, {s - x[i]})')
        print('Result: True')
        print('\n')
        return True
    else:
        print(f'Q({i}, {s}) => Checked if Q({i - 1}, {s}) or ({x[i]} == {s}) or Q({i - 1}, {s - x[i]})')
        print('Result: False')
        print('\n')
        return False


if __name__ == '__main__':    
    N = 123  # number of integers
    min_integer = -10
    max_integer = 10
    S = 0  # initial sum to achieve
    X = [random.randint(min_integer, max_integer) for i in range(N)]  # list of random integers from min_integer to max_integer
    index = 3

    print('---------------------------------------')

    print(f'List of N={N} random integers, X, where {min_integer} <= X_i <= {max_integer}: {X}\n')

    print(f'S={S}\n')

    print(f'Trying index = {index}\n')

    result = Q(x=X, i=index, s=S)

    print(f'Final Result: {result}')

    print('---------------------------------------')
