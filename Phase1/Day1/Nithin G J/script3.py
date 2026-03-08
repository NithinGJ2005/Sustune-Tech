#This script creates a dictionary of marks for three subjects,then calculates and prints the total and average marks.

# Create dictionary
marks = {
        "maths": 90,
        "science": 90,
        "kannade": 100
}

# Calculate total marks
total = sum(marks.values())

# Calculate average marks
average = total / len(marks)

# Print results
print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
