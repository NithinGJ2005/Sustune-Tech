# This script creates a list of courses, adds a new course,removes one course, and prints the final list.

# Create a list with 5 course names
courses = ["Python", "Data Structures", "Machine Learning", "NLP", "Operating Systems"]

# Add one more course
courses.append("Deep Learning")
print("After adding one course:",courses)

# Remove one course
courses.remove("NLP")
print("After removing one course:",courses)

# Print the final list
print("Final Course List:", courses)
