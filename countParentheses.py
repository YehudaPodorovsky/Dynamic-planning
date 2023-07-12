def countParentheses(expression):
    n = len(expression)
    T = [[0] * n for _ in range(n)]
    F = [[0] * n for _ in range(n)]

    for i in range(n):
        if expression[i] == 'T':
            T[i][i] = 1
        else:
            F[i][i] = 1

    for length in range(3, n+1, 2):
        for i in range(0, n-length+1, 2):
            j = i + length - 1
            for k in range(i+1, j, 2):
                operator = expression[k]
                print(i, k-1, expression[k], k+1, j)
                if operator == '&':
                    T[i][j] += T[i][k-1] * T[k+1][j]
                    F[i][j] += (F[i][k-1] * F[k+1][j]
                                + F[i][k-1] * T[k+1][j]
                                + T[i][k-1] * F[k+1][j])
                elif operator == '|':
                    T[i][j] += (T[i][k-1] * T[k+1][j]
                                + T[i][k-1] * F[k+1][j]
                                + F[i][k-1] * T[k+1][j])
                    F[i][j] += F[i][k-1] * F[k+1][j]
                elif operator == '^':
                    T[i][j] += (T[i][k-1] * F[k+1][j]
                                + F[i][k-1] * T[k+1][j])
                    F[i][j] += (T[i][k-1] * T[k+1][j]
                                + F[i][k-1] * F[k+1][j])
                print("True table\t\t\t", "False table")
                for h in range(len(T)):
                    print(T[h], "\t", F[h])
    return T[0][n-1]


# Example usage:
boolean_expression = "F&T^T"
result = countParentheses(boolean_expression)
print("Maximum number of true evaluations:", result)
