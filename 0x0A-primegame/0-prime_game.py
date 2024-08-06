#!/usr/bin/python3
"""
Prime Game module
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Parameters:
    x (int): The number of rounds.
    nums (list): An array of integers representing the upper
    limit of the set for each round.

    Returns:
    str: The name of the player that won the most rounds,
    or None if no winner can be determined.
    """
    if x <= 0 or not nums:
        return None

    # Determine the maximum number in nums to limit sieve size
    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    # Sieve of Eratosthenes to find all primes up to max_num
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # List of prime counts up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    # Determine the winner for each game
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
