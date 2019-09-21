"""
A stock is a security that indeicates ownership in a company. Publicly traded stocks have an associated price that
typically changes daily.
Suppose you are given a list of integers, prices, that represent the price of Google's stock over time. prices[i] is the price
of the stock on day i. You must buy the stock once and then later sell it. You are not allowed to sell before you buy.

Write a function that returns an integer, which is the maximum profit you can make from buying the stock and then later selling it.
If the list is empty, return 0.

Example Input:

price = [6, 0, -1, 10]

Example Output:

11

Explanation:

11 is the maximum profit you can make by buying the stock when it's -1 and selling it when it's 10.

"""

def solution(prices):
    # Type your solution here
    max_profit = -1
    for i in range(len(prices)):
        for j in range(len(prices)):
            first_number = prices[i]
            second_number = prices[j]
            # If the two numbers are the same index and
            # the first index is less than the second index (we bought before we sold)
            if i != j and i < j and first_number < second_number:
                difference = second_number - first_number
                if difference > max_profit:
                    max_profit = difference
    return max_profit



if __name__ == '__main__':
    prices = [6, 0, -1, 10]
    print(solution(prices))
