#!/usr/bin/python3
""" module containing makeChange function """


def makeChange(coins, total):
    """
    makeChange function
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total

    Parameters:
    -coins: list of the values of the coins in your possession
    -total: given amount to be met

    Returns:
    fewest number of coins needed to meet total
    -If total is 0 or less, return 0
    -If total cannot be met by any number of coins you have,
    return -1
    """

    if not coins or coins is None:
        return -1

    if total <= 0:
        return 0

    change = 0
    coins = sorted(coins)[::-1]

    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
