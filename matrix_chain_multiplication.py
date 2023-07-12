def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1

    # Create matrices to store results and split positions
    # Initialize them with zeros
    cost = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]

    # Solve subproblems
    for chain_len in range(2, n + 1):
        for i in range(1, n - chain_len + 2):
            j = i + chain_len - 1
            cost[i][j] = float('inf')

            for k in range(i, j):
                # Calculate the cost of splitting at position k
                current_cost = cost[i][k] + cost[k+1][j] + dimensions[i-1] * dimensions[k] * dimensions[j]

                if current_cost < cost[i][j]:
                    # Update the minimum cost and split position
                    cost[i][j] = current_cost
                    split[i][j] = k
    # print("cost")
    # for i in range(len(cost)):
    #     print(cost[i])
    # print("split")
    # for i in range(len(cost)):
    #     print(split[i])
    # Build the optimal solution
    def build_solution(i, j):
        if i == j:
            return "A" + str(i)

        k = split[i][j]
        left_chain = build_solution(i, k)
        right_chain = build_solution(k+1, j)

        return "(" + left_chain + " x " + right_chain + ")"

    # Return the optimal solution and total cost
    optimal_solution = build_solution(1, n)
    total_cost = cost[1][n]

    return optimal_solution, total_cost

# Example usage
matrix_dimensions = [10, 30, 5, 60]
optimal_order, minimum_cost = matrix_chain_multiplication(matrix_dimensions)

print("Optimal Order of Multiplication:", optimal_order)
print("Minimum Cost:", minimum_cost)
