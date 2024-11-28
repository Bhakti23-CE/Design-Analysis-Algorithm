'''Problem Statement 
Consider a XYZ courier company. They receive different goods to transport to different cities. 
Company needs to ship the goods based on their life and value. 
Goods having less shelf life and high cost shall be shipped earlier. 
Consider a list of 100 such items and the capacity of a transport vehicle is 200 tons. 
Implement Algorithms for fractional knapsack problems.
'''
import csv


class Item:
    def __init__(self, name, value, weight, shelf_life):
        self.name = name
        self.value = value
        self.weight = weight
        self.shelf_life = shelf_life
        self.value_per_weight = value / weight if weight != 0 else 0


# Function to perform the fractional knapsack algorithm
def fractional_knapsack(items, capacity):
    try:
        if capacity <= 0:
            raise ValueError("The capacity of the knapsack must be greater than zero.")
       
        # Sort items by the ratio of (1 / shelf_life) * value_per_weight in descending order
        items.sort(key=lambda x: (1 / x.shelf_life) * x.value_per_weight, reverse=True)


        total_value = 0.0
        selected_items = []  # List to store selected items and fractions


        for item in items:
            if capacity <= 0:
                break
           
            # Check if the whole item can be taken
            if item.weight <= capacity:
                total_value += item.value
                capacity -= item.weight
                selected_items.append((item, 1))  # 1 indicates full item taken
            else:
                # Take the fractional part of the item
                fraction = capacity / item.weight
                total_value += item.value * fraction
                selected_items.append((item, fraction))  # Store item with fraction taken
                capacity = 0


        # Display all data of selected items
        print("\nSelected items:")
        for item, fraction in selected_items:
            print(f"Item: {item.name}, Value: {item.value}, Weight: {item.weight}, Shelf Life: {item.shelf_life}, Fraction Taken: {fraction:.2f}")


        print(f"\nTotal value in knapsack: {total_value:.2f}")
        return total_value


    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Function to read items from a CSV file
def read_items_from_csv(file_path):
    items = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    name = row['name']
                    value = float(row['value'])
                    weight = float(row['weight'])
                    shelf_life = int(row['shelf_life'])
                    items.append(Item(name, value, weight, shelf_life))
                except ValueError as e:
                    print(f"Error processing row {row}: {e}")
                except KeyError as e:
                    print(f"Missing expected column {e} in CSV row: {row}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"Unexpected error reading the file: {e}")
    return items


# Path to the CSV file (adjust the path as needed)
csv_file_path = 'items.csv'


# Read items from the CSV file
items = read_items_from_csv(csv_file_path)


if items:  # Proceed only if items were successfully read
    # Capacity of the transport vehicle
    capacity = 200  # in tonnes


    # Execute the algorithm
    fractional_knapsack(items, capacity)
else:
    print("No items available to process.")
