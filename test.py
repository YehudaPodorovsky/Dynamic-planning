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


# Example input matrix
input_matrix = [[9, 2, 3], [4, 5, 6], [7, 8, 1]]

output = diagonal_scan(input_matrix)
print(output)
