# LCS
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    OPT = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                OPT[i][j] = OPT[i - 1][j - 1] + 1
            else:
                OPT[i][j] = max(OPT[i - 1][j], OPT[i][j - 1])

    print("OPT table")
    for i in range(len(OPT)):
        print(OPT[i])
    # Reconstruct the longest common subsequence
    print()
    printLCSReco(OPT, m, j)
    print()
    return printLCSiter(OPT, text1, text2, m, n)

def printLCSiter(OPT, text1, text2, i, j):
    lcs = []
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.insert(0, text1[i - 1])
            i -= 1
            j -= 1
        elif OPT[i - 1][j] > OPT[i][j - 1]:
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

# text1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
# text2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
text1 = "ABCBDAB"
text2 = "BDCABA"
print(longest_common_subsequence(text1, text2))

