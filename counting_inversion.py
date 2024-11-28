'''Problem Statement
Consider first/second year course-code choices of 100 students. 
Find the inversion count of these choices.
Find students with zero, one, two, three inversion counts and comment on your result.
'''
import csv


def merge_count_split_inv(arr, temp_arr, left, right):
    """Merge step that counts the inversions between the two halves."""
    if left == right:
        return 0
    mid = (left + right) // 2
    inv_count = merge_count_split_inv(arr, temp_arr, left, mid)
    inv_count += merge_count_split_inv(arr, temp_arr, mid + 1, right)
    inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    return inv_count


def merge_and_count(arr, temp_arr, left, mid, right):
    """Merge the two sorted halves and count inversions."""
    i = left    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = left    # Starting index to be sorted
    inv_count = 0
   
    # Merge the two subarrays
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # All remaining elements in left subarray are greater than arr[j]
            j += 1
        k += 1


    # Copy the remaining elements of left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1


    # Copy the remaining elements of right subarray, if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1


    # Copy the sorted subarray into the original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
   
    return inv_count


def count_inversions(arr):
    """Main function to count inversions using divide and conquer (merge sort)."""
    n = len(arr)
    temp_arr = [0] * n
    return merge_count_split_inv(arr, temp_arr, 0, n - 1)


def process_student_data(filename):
    """Process the student data and count inversions for each student."""
    inversion_counts = {0: 0, 1: 0, 2: 0, 3: 0, 'greater_than_3': 0}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                try:
                    # Convert the course choices to integers
                    course_choices = list(map(int, row[1:]))  # Assuming course codes are in columns 2 onward
                    inv_count = count_inversions(course_choices)
                    # Categorize based on inversion count
                    if inv_count in inversion_counts:
                        inversion_counts[inv_count] += 1
                    else:
                        inversion_counts['greater_than_3'] += 1
                except ValueError:
                    print(f"Error: Invalid data in row {row}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    return inversion_counts


def main():
    # Filepath to the CSV file containing student data
    filename = 'student_course_choices.csv'
    inversion_counts = process_student_data(filename)
   
    # Output the inversion counts
    for inv_count, count in inversion_counts.items():
        print(f"Students with {inv_count} inversions: {count}")


if __name__ == "__main__":
    main()
