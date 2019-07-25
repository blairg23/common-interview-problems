"""
Solves a basic subset sum problem using dynamic programming.

The subset sum problem is this:

Given a list X and index i, is there a nonempty subset of X_1,...,X_i which sums to S?
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
        print(f'Base Case: Checking if {x[i]} == {s}')
        if x[i] == s:
            print('Result: True')
            print('\n')
            return True
        else:
            print('Result: False')
            print('\n')
            return False

    print(f'Checking if Q({i - 1}, {s}) or ({x[i]} == {s}) or Q({i - 1}, {s - x[i]})\n')
    if Q(x, i - 1, s) or (x[i] == s) or Q(x, i - 1, s - x[i]):
        print(f'Checked if Q({i - 1}, {s}) or ({x[i]} == {s}) or Q({i - 1}, {s - x[i]})')
        print('Result: True')
        print('\n')
        return True
    else:
        print(f'Checked if Q({i - 1}, {s}) or ({x[i]} == {s}) or Q({i - 1}, {s - x[i]})')
        print('Result: False')
        print('\n')
        return False


if __name__ == '__main__':    
    N = number_of_integers = 123
    max_integer = 10
    min_integer = -10
    S = requested_sum = 0
    X = list_of_integers = [random.randint(min_integer, max_integer) for i in range(number_of_integers)]
    index = 5

    print('---------------------------------------')

    print(f'List of N={N} random integers, X, where {min_integer} <= X_i <= {max_integer}: {X}')

    print(f'S={S}')

    print(f'Trying index = {index}')

    result = Q(x=X, i=index, s=S)

    print(f'Final Result: {result}')

    print('---------------------------------------')
