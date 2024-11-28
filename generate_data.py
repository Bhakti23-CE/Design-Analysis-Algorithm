import csv
import random


def generate_student_data(num_students, num_courses, filename):
    """Generate random course choices for students and save to a CSV file."""
    # Open the file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
       
        # Write the header
        writer.writerow(["StudentID", "Course1", "Course2", "Course3", "Course4"])
       
        # Generate random course choices for each student
        for student_id in range(1, num_students + 1):
            # Randomly assign courses from the range [1, num_courses]
            courses = random.sample(range(1, num_courses + 1), num_courses)
           
            # Write the student ID and their course choices
            writer.writerow([student_id] + courses)


# Parameters: 100 students, 4 courses
generate_student_data(100, 4, 'student_course_choices.csv')
