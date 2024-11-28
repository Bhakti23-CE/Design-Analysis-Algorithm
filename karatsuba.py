'''Problem Statement
Consider large integers of size 10, 50, 100, 500 and 1000 digits. 
Write integer multiplication program 
Write an integer multiplication program using divide and conquer technique.
'''
def karatsuba(x, y):
    # Convert the numbers to strings to easily split them
    x_str = str(x)
    y_str = str(y)
   
    # Base case for recursion
    if len(x_str) == 1 or len(y_str) == 1:
        return x * y
   
    # Length of the numbers
    n = max(len(x_str), len(y_str))
    m = n // 2
   
    # Split the numbers
    x_high = int(x_str[:-m]) if len(x_str) > m else 0
    x_low = int(x_str[-m:])
    y_high = int(y_str[:-m]) if len(y_str) > m else 0
    y_low = int(y_str[-m:])
   
    # Recursive calls to calculate the three products
    p1 = karatsuba(x_high, y_high)
    p2 = karatsuba(x_low, y_low)
    p3 = karatsuba(x_high + x_low, y_high + y_low)
   
    # Combine the results
    return p1 * 10*(2 * m) + (p3 - p1 - p2) * 10*m + p2


# Example usage with user inputs
if __name__ == "__main__":
    try:
        # Taking user inputs
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
       
        # Call the Karatsuba multiplication function
        result = karatsuba(x, y)
       
        # Print the result
        print(f"Product of {x} and {y} is: {result}")
    except ValueError:
        print("Invalid input. Please enter valid integers.")
