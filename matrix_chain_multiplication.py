'''Consider meteorological data like temperature, dew point, wind direction, wind speed, cloud cover, cloud layer(s) for each city. 
This data is available in two dimensional array for a week. Assuming all tables are compatible for multiplication. 
You have to implement the matrix chain multiplication algorithm to 
find fastest way to complete the matrices multiplication to achieve timely predication.
'''
def matrix_chain_order(p):
    # Error handling for invalid input
    if not p or len(p) < 2:
        raise ValueError("Input list p must contain at least two elements representing matrix dimensions.")
   
    n = len(p) - 1  # Number of matrices
   
    # Initialize m and s tables
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
   
    # l is the chain length
    for length in range(2, n + 1):  # length of chain from 2 to n
        for i in range(n - length + 1):  # i is the starting index of the chain
            j = i + length - 1  # j is the ending index of the chain
           
            m[i][j] = float('inf')  # Initialize to infinity
           
            # Try every possible split
            for k in range(i, j):
                # Calculate the cost of splitting at k
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
               
                # If this is the minimal cost, update m[i][j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
   
    # Return the minimum number of multiplications and the split table
    return m, s


def print_optimal_parenthesization(s, i, j):
    if i == j:
        print(f"A{i+1}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(s, i, s[i][j])
        print_optimal_parenthesization(s, s[i][j] + 1, j)
        print(")", end="")

# 7 days of data for each city
p = [7, 5, 6, 4, 3]  # Example matrix dimensions (can be modified as needed)


# Perform matrix chain multiplication
m, s = matrix_chain_order(p)


# Print the result
print(f"Minimum number of scalar multiplications: {m[0][-1]}")
print("Optimal parenthesization: ", end="")
print_optimal_parenthesization(s, 0, len(p) - 2)
