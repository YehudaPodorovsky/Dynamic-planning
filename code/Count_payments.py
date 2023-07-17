# Count payments

def count_payments(c, n):
    OPT = [0] * (n + 1)
    OPT[0] = 1

    for i in range(n + 1):
        for j in c:
            OPT[i] += OPT[i - j]

    print(OPT)



c = [1, 3, 5]
n = 11
count_payments(c, n)
