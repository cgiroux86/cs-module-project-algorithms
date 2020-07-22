#!/usr/bin/python

import sys


def making_change(amount, denominations, idx=0):
    print(amount, denominations, idx)
    # Your code here
    if amount < 0 or idx == len(denominations):
        return 0
    if amount == 0:
        return 1
    else:
        print('amount', amount, idx)
        first = making_change(
            amount - denominations[idx], denominations, idx)
        rest = making_change(
            amount, denominations, idx=idx + 1)
    return first + rest


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
