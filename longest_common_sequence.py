'''Problem Statement
Consider grades received by 20 students,  like AA, AB, BB, ..., FF of each student.
Computer the Longest common sequence of grades among students.
'''
def lcs(X, Y):
    try:
        # Validate inputs
        if not isinstance(X, str) or not isinstance(Y, str):
            raise ValueError("Both input sequences must be strings.")


        m, n = len(X), len(Y)
       
        # Create a 2D table to store lengths of longest common subsequence.
        dp = [[0] * (n + 1) for _ in range(m + 1)]
       
        # Fill the table in a bottom-up manner
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1  # If characters match, add 1 to the result from the previous diagonal
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # Otherwise, take the maximum of the left or top
       
        # Reconstruct the LCS from the dp table
        lcs_result = []
        i, j = m, n
        while i > 0 and j > 0:
            if X[i - 1] == Y[j - 1]:
                lcs_result.append(X[i - 1])  # Add the character to the result
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
       
        # Return the LCS result as a string
        return ''.join(reversed(lcs_result))  # Reverse because we built the LCS backwards


    except Exception as e:
        print(f"Error in LCS calculation: {e}")
        return ""




def lcs_of_all_students(grades):
    try:
        # Validate input grades list
        if not grades:
            raise ValueError("The grades list cannot be empty.")
       
        if not all(isinstance(grade, str) for grade in grades):
            raise ValueError("Each grade must be a string.")
       
        # Start with the first student's grades
        common_lcs = grades[0]
        print(f"Initial common LCS: {common_lcs}")
       
        # Compute LCS with each subsequent student's grades
        for grade in grades[1:]:
            print(f"Current common LCS: {common_lcs} with student grade: {grade}")
            common_lcs = lcs(common_lcs, grade)
            if not common_lcs:  # If at any point, the LCS becomes empty, break early
                break
            print(f"Updated common LCS: {common_lcs}")
       
        return common_lcs


    except Exception as e:
        print(f"Error in LCS calculation for all students: {e}")
        return ""




def main():
        # Example grades for 20 students
        grades = [
            "AA", "AB", "BB", "BC", "CD", "DE", "EF", "FA", "AA", "BB",
            "AA", "BA", "CC", "AB", "EF", "BA", "BC", "CD", "AA", "AA"
        ]
       
        # Compute LCS for all students
        common_lcs = lcs_of_all_students(grades)
       
        if common_lcs:
            print(f"Longest Common Subsequence of grades: {common_lcs}")
        else:
            print("No common subsequence found among students.")


if __name__ == "__main__":
    main()
