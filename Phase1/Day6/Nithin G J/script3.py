#attendance.csv

try:
    attendance_count = {}
    highest = 0
    best_student = ""

    with open("attendance.csv", "r") as infile, open("attendance_report.csv", "w") as outfile:

        header = infile.readline().strip()
        outfile.write(header + "\n")   

        for line in infile:
            line = line.strip()

            if not line:
                continue

            name, date, status = line.split(",")

            status = status.strip()
            if status == "P":
                status = "Present"
            elif status == "A":
                status = "Absent"
            elif status not in ["Present", "Absent"]:
                print("Invalid status for", name)
                continue

            outfile.write(f"{name},{date},{status}\n")

            if status == "Present":
                if name in attendance_count:
                    attendance_count[name] += 1
                else:
                    attendance_count[name] = 1

    print("\nAttendance Summary:")

    for name in attendance_count:
        print(name, "Present Days:", attendance_count[name])

        if attendance_count[name] > highest:
            highest = attendance_count[name]
            best_student = name

    print("Highest Attendance:", best_student, "->", highest)

except FileNotFoundError:
    print("Error: attendance.csv file not found")

except Exception as e:
    print("Error:", e)