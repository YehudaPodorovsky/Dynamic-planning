# Count hems by count prime factors
def count_hems(n, num):
    OPT = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        OPT[i][1] = 1
        for j in range(2, i + 1):
            OPT[i][j] = OPT[i-1][j] * j + OPT[i - 1][j - 1]

    for i in range(n + 1):
        print(OPT[i])
    print("The number of ways to factorize the number", num, "is:", sum(OPT[i]))

def count_prime_factors(num):
    number = num
    count = 0
    i = 2  # Start with the smallest prime number

    while i * i <= num:
        if num % i == 0:
            count += 1
            while num % i == 0:
                num //= i  # Divide the number by the prime factor
        i += 1

    if num > 1:
        count += 1

    count_hems(count, number)

number = 30
count_prime_factors(number)
