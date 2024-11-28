# Function to calculate CPI
def calculate_cpi(spi_list, credit_list):
    total_spi_credits = 0
    total_credits = 0

    for spi, credits in zip(spi_list, credit_list):
        total_spi_credits += spi * credits
        total_credits += credits

    if total_credits == 0:
        return "Error: Total credits cannot be zero"
    
    CPI = total_spi_credits / total_credits
    return CPI

# Main program
def main():
    spi_list = []
    credit_list = []
    num_semesters = int(input("Enter the number of semesters: "))
    
    for i in range(num_semesters):
        spi = float(input(f"Enter SPI for semester {i + 1}: "))
        credits = int(input(f"Enter total credits for semester {i + 1}: "))
        spi_list.append(spi)
        credit_list.append(credits)

    cpi = calculate_cpi(spi_list, credit_list)
    print(f"CPI: {cpi}")

# Run the program
if __name__ == "__main__":
    main()
