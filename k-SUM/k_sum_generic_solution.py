"""
Another subset sum problem solution! https://en.wikipedia.org/wiki/Subset_sum_problem

Similar to the 3SUM problem from https://en.wikipedia.org/wiki/3SUM,

this solves the k-SUM problem using a generic solution:

Given a set of N real numbers, are there any k number of elements that sum to zero.

Solves in O(n^2).

This is the Python implementation of a Java solution proposed in:

https://skyxu.me/2018/08/05/a-generic-solution-to-k-sum-problems/
"""

import random


class KSum:
    """
    Given a set of numbers, find all k elements groups that add up to the given target.
    """
    def __init__(self):
        pass

    def k_sum(self, numbers, k, target):
        """

        :param list numbers: A list of positive and negative integers.
        :param int k: The number of elements per group that should add up to the given target.
        :param int target: The target sum value.
        :return set: All k elements groups that add up to the given target.
        """
        numbers = sorted(numbers)
        if k <= 1:
            k_integers = []
            if k == 1 and numbers.index(target) >= 0:
                k_integers.append([target])
            return k_integers
        return self._k_sum_helper(numbers=numbers, k=k, target=target, begin_index=0)

    def _k_sum_helper(self, numbers, k, target, begin_index):
        """

        :param list numbers: A list of positive and negative integers.
        :param int k: The number of elements per group that should add up to the given target.
        :param int target: The target sum value.
        :param begin_index: The index to start on.
        :return: All groups of k elements from begin_index that add up to the given target.
        """
        N = len(numbers)
        if k == 2:
            k_integers = []
            left = begin_index
            right = N - 1
            while (left < right):
                number_sum = numbers[left] + numbers[right]
                if number_sum == target:
                    k_integers.append([numbers[left], numbers[right]])
                    while left < right and numbers[left] == numbers[left + 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif number_sum < target:
                    left += 1
                else:
                    right -= 1
            return k_integers

        k_integers = []
        for i in range(begin_index, N - k):
            if (i > begin_index and numbers[i] == numbers[i - 1]) or (numbers [i] + (k - 1) * numbers[N - 1] < target):
                continue
            if (numbers[i] + (k - 1) * numbers[i + 1] > target):
                break
            sub = self._k_sum_helper(numbers=numbers, k=k-1, target=target - numbers[i], begin_index=i+1)
            for sub_list in sub:
                sub_list.insert(0, numbers[i])
            k_integers.extend(sub)
        return k_integers




if __name__ == '__main__':
    N = 123  # number of integers
    min_integer = -10
    max_integer = 10
    X = [random.randint(min_integer, max_integer) for i in range(N)]  # list of random integers from min_integer to max_integer
    k_integers = set()  # Set to hold the unique k-sized groups of integers that sum to zero
    K = 4
    S = 0

    print('---------------------------------------')

    print(f'List of N={N} random integers, X, where {min_integer} <= X_i <= {max_integer}: {X}\n')

    print(f'K={K}\n')

    print(f'S={S}\n')

    k_sum = KSum()
    result = k_sum.k_sum(numbers=X, k=K, target=S)

    print(f'Final Result: {result}')

    print('---------------------------------------')