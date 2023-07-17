# Minimum coins
def minimum_coins(coins, x):
    OPT = [[0] * (x + 1) for _ in range(len(coins) + 1)]

    for i in range(len(OPT)):
        for j in range(1, x + 1):
            if i == 0:
                OPT[i][j] = j
            elif j < coins[max(0, i - 1)]:
                OPT[i][j] = OPT[i - 1][j]
            else:
                OPT[i][j] = min(OPT[i - 1][j], 1 + OPT[i][j - coins[max(0, i - 1)]])

    for i in range(len(OPT)):
        print(OPT[i])
    print(f"Given the coin series {coins} and we would like to pay NIS {x}, the minimum number of coins is {OPT[i][j]}.")

coins = [1, 4, 5]
x = 8
minimum_coins(coins, x)
