from itertools import combinations_with_replacement

def find_minimum_coins(total_change, coins):
    coins.sort()
    if total_change < coins[0] and total_change != 0:
        raise ValueError("Incorrect total_change value")
    for i in range(total_change//coins[0] + 1):
        for comb in combinations_with_replacement(coins, i):
            if sum(comb) == total_change:
                return list(comb)
    raise ValueError("Combination was not found")
