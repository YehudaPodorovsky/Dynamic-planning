# Coin game
def coin_game(v):
    n = len(v)
    OPT = [[None] * n for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(n):
            if i == j:
                OPT[i][i] = v[i]
            elif i + 1 == j:
                OPT[i][j] = max(OPT[i+1][j], OPT[i][j-1])
            elif i < j:
                OPT[i][j] = max(OPT[i][j-(j-i)] + min(OPT[i+2][j], OPT[i+1][j-1]), OPT[i+(j-i)][j] + min(OPT[i][j-2], OPT[i+1][j-1]))

    for i in range(len(OPT)):
        print(OPT[i])
    print("solution:", OPT[0][len(OPT)-1])

v = [10, 20, 5, 4]
coin_game(v)
