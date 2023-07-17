# Max_palindrome

def max_palindrome(text):
    n = len(text)

    OPT = [[0] * n for _ in range(n)]
    for i in range(n):
        OPT[i][i] = 1
    for i in range(n):
        for j in range(i):
            if text[i].__eq__(text[j]):
                OPT[j][i] = OPT[i][j] = OPT[i - 1][j + 1]

    print("OPT table")
    for i in range(n):
        print(OPT[i])

    print()
    print("OPT diagonal table")
    OPT_diagonal = diagonal_scan(OPT)
    maxstring = 1
    end = n
    for i in range(len(OPT_diagonal)):
        if sum(OPT_diagonal[i]) == len(OPT_diagonal[i]) and maxstring < len(OPT_diagonal[i]):
            maxstring = len(OPT_diagonal[i])
            end = i
        print(OPT_diagonal[i])
    print()
    print(f"The longest sequence is {maxstring} characters:", text[end - n + 1:end + 1])

def diagonal_scan(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    output = []

    # Scan upper diagonals
    for c in range(cols):
        diagonal = []
        i = 0
        j = c
        while i < rows and j >= 0:
            diagonal.append(matrix[i][j])
            i += 1
            j -= 1
        output.append(diagonal)

    # Scan lower diagonals
    for r in range(1, rows):
        diagonal = []
        i = r
        j = cols - 1
        while i < rows and j >= 0:
            diagonal.append(matrix[i][j])
            i += 1
            j -= 1
        output.append(diagonal)

    return output



text1 = "אאנטולגלוטנ"
max_palindrome(text1)

