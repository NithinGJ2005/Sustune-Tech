
with open("attendance.csv", "w") as f:
    f.write("Name,Date,Status\n")
    f.write("vinay,2026-02-01,P\n")
    f.write("Rahul,2026-02-01,A\n")
    f.write("vinay,2026-02-02,Present\n")
    f.write("Rahul,2026-02-02,Absent\n")
    f.write("Ananya,2026-02-02,X\n")  


def process_attendance_csv():
    try:
        attendance_count = {}

        with open("attendance.csv", "r") as infile, open("attendance_report.csv", "w") as outfile:
            header = infile.readline().strip()
            outfile.write(header + "\n")

            for line in infile:
                line = line.strip()
                if not line:
                    continue

                name, date, status = line.split(",")
                status = status.upper()

                if status == "P":
                    status = "Present"
                elif status == "A":
                    status = "Absent"
                elif status not in ["PRESENT", "ABSENT"]:
                    print("Invalid status for", name)
                    continue

                if status.lower() == "present":
                    attendance_count[name] = attendance_count.get(name, 0) + 1

                outfile.write(f"{name},{date},{status}\n")

        print("\n--- Attendance Summary ---")
        highest_name = ""
        highest_days = -1

        for name, days in attendance_count.items():
            print(name, "Present Days:", days)
            if days > highest_days:
                highest_days = days
                highest_name = name

        if highest_name:
            print("Highest Attendance:", highest_name, highest_days)

    except FileNotFoundError:
        print("Attendance file not found.")


process_attendance_csv()