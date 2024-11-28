''' Problem Statement: 
Write an algorithm to find gross and net salary of employees.
ABC co. ltd. has 2000 employees. 
Your task is to calculate each employee's salary and find employees with minimum salary and maximum salary.
Do the above task using  divide and conquer technique. 
'''

import csv
# Employee class to store employee data and calculate salaries
class Employee:
   def __init__(self, emp_id, base_salary, house_rent_allowance, medical_allowance, transport_allowance, tax, insurance, loan_repayment):
       self.emp_id = emp_id
       # Ensure all salary components are non-negative
       self.base_salary = max(0, base_salary)
       self.house_rent_allowance = max(0, house_rent_allowance)
       self.medical_allowance = max(0, medical_allowance)
       self.transport_allowance = max(0, transport_allowance)
       self.tax = max(0, tax)
       self.insurance = max(0, insurance)
       self.loan_repayment = max(0, loan_repayment)


   @property
   def gross_salary(self):
       return (self.base_salary + self.house_rent_allowance +
               self.medical_allowance + self.transport_allowance)


   @property
   def net_salary(self):
       total_deductions = self.tax + self.insurance + self.loan_repayment
       return self.gross_salary - total_deductions


def read_employee_data_from_csv(filename):
   employees = []
   with open(filename, mode='r') as file:
       reader = csv.DictReader(file)
       for row_num, row in enumerate(reader, start=1):
           try:
               # Create Employee instance and validate for non-negative values
               employee = Employee(
                   emp_id=row['Employee ID'],
                   base_salary=float(row['Base Salary']),
                   house_rent_allowance=float(row['House Rent Allowance']),
                   medical_allowance=float(row['Medical Allowance']),
                   transport_allowance=float(row['Transport Allowance']),
                   tax=float(row['Tax']),
                   insurance=float(row['Insurance']),
                   loan_repayment=float(row['Loan Repayment'])
               )
               employees.append({
                   'Employee ID': employee.emp_id,
                   'Base Salary': employee.base_salary,
                   'House Rent Allowance': employee.house_rent_allowance,
                   'Medical Allowance': employee.medical_allowance,
                   'Transport Allowance': employee.transport_allowance,
                   'Tax': employee.tax,
                   'Insurance': employee.insurance,
                   'Loan Repayment': employee.loan_repayment,
                   'Gross Salary': employee.gross_salary,
                   'Net Salary': employee.net_salary,
               })
           except ValueError as e:
               print(f"Invalid data format detected in row {row_num}: {row}. Error: {e}")
   return employees


# Divide and conquer function to find min/max salaries
def find_min_max_divide_conquer(employees, low, high):
   # Base case: when only one employee is left, return them as both min and max
   if low == high:
       return employees[low], employees[low]
  
   # Divide: split the array into two halves
   mid = (low + high) // 2
   min_left, max_left = find_min_max_divide_conquer(employees, low, mid)
   min_right, max_right = find_min_max_divide_conquer(employees, mid + 1, high)
  
   # Conquer: compare and return the overall min and max
   min_salary_employee = min(min_left, min_right, key=lambda x: x['Net Salary'])
   max_salary_employee = max(max_left, max_right, key=lambda x: x['Net Salary'])
  
   return min_salary_employee, max_salary_employee


def print_employee_details(employee, salary_type):
   print(f"\nEmployee with {salary_type} Salary:")
   print({
       "Employee ID": employee['Employee ID'],
       "Gross Salary": employee['Gross Salary'],
       "Net Salary": employee['Net Salary']
   })


def save_to_same_csv(filename, employees):
   # Overwrite the same file with the updated employee data
   with open(filename, mode='w', newline='') as file:
       writer = csv.DictWriter(file, fieldnames=employees[0].keys())
       writer.writeheader()
       writer.writerows(employees)


def main():
   # Prompt user to input the CSV file path
   input_filename = input("Please enter the path of the CSV file: ")
  
   # Read employee data from the provided CSV file
   employees = read_employee_data_from_csv(input_filename)
  
   if employees:
       # Use divide and conquer to find min and max salary employee
       min_employee, max_employee = find_min_max_divide_conquer(employees, 0, len(employees) - 1)
      
       # Print min/max salary employee with detailed info
       print_employee_details(min_employee, "Minimum")
       print_employee_details(max_employee, "Maximum")
  
       # Save changes to the same CSV  file
       save_to_same_csv(input_filename, employees)
       print(f"Changes have been saved to '{input_filename}'.")
   else:
       print("No employee data found to process.")


if __name__ == "__main__":
   main()
