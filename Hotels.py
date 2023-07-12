import sys

def calculate_effort(distance):
    return distance**2

def select_hotel_locations(hotel_distances, max_days):
    n = len(hotel_distances)

    # Initialize a matrix to store the minimum effort for each subproblem
    dp = [[sys.maxsize] * (n + 1) for _ in range(max_days + 1)]
    dp[0][0] = 0

    # Perform dynamic programming
    for i in range(1, max_days + 1):
        for j in range(1, n + 1):
            for k in range(j, 0, -1):
                distance = hotel_distances[j-1] - hotel_distances[k-1]
                if distance <= i:
                    effort = calculate_effort(distance)
                    dp[i][j] = min(dp[i][j], dp[i-1][k-1] + effort)

    # Find the optimal solution
    optimal_track_length = hotel_distances[-1]

    return dp, optimal_track_length

# Example usage
hotel_distances = [1, 2, 4, 7]
max_days = 2

dp_matrix, track_length = select_hotel_locations(hotel_distances, max_days)
print("Dynamic Programming Matrix:")
for row in dp_matrix:
    print(row)
print("Total Track Length:", track_length)
