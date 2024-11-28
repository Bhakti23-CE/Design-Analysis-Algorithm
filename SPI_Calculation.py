# Function to calculate SPI
def calculate_spi(cp_list, gp_list):
    total_sum = 0
    total_credits = 0

    # Calculate total sum and total credits
    for CP, GP in zip(cp_list, gp_list):
        total_sum += CP * GP
        total_credits += CP

    # Check for division by zero
    if total_credits == 0:
        return "Error: Total credits cannot be zero"
    
    # Calculate SPI
    SPI = total_sum / total_credits
    return SPI

# Main program
def main():
    cp_list = []
    gp_list = []
    num_subjects = int(input("Enter the number of subjects: "))

    # Get user input for CP and GP for each subject
    for i in range(num_subjects):
        CP = int(input(f"Enter credit points for subject {i + 1}: "))
        GP = int(input(f"Enter grade points for subject {i + 1} (0-10): "))
        cp_list.append(CP)
        gp_list.append(GP)

    # Call the function with CP and GP lists
    spi = calculate_spi(cp_list, gp_list)
    print(f"SPI: {spi}")

if __name__ == "__main__":
    main()

