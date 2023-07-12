def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    for i in range(len(dp)):
        print(dp[i])
    # Reconstruct the longest common subsequence
    printLCSReco(dp, m, j)
    print()

    return printLCSiter(dp, text1, text2, m, n)

def printLCSiter(dp, text1, text2, i, j):
    lcs = []
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.insert(0, text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return lcs

def printLCSReco(b, i, j):
    if i == 0 or j == 0:
        return
    if text1[i - 1] == text2[j - 1]:
        printLCSReco(b, i-1, j-1)
        print(text1[i - 1], end=" ")
    elif b[i - 1][j] > b[i][j - 1]:
        printLCSReco(b, i-1, j)
    else:
        printLCSReco(b, i, j-1)

# Example usage:
# text1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
# text2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
text1 = "ABCBDAB"
text2 = "BDCABA"
result = longest_common_subsequence(text1, text2)
print(result)  # Output: ['A', 'D', 'H']
