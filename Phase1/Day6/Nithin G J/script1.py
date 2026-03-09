def process_students_csv():
    try:
        total_marks = 0
        count = 0
        topper_name = ""
        topper_marks = -1

        with open("students.csv", "r") as infile, open("students_report.csv", "w") as outfile:
            header = infile.readline().strip()
            outfile.write(header + ",Result,Grade\n")

            for line in infile:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) != 3:
                    continue

                name, age, marks_str = parts

                try:
                    marks = int(marks_str)
                except ValueError:
                    raise ValueError(f"Invalid marks value for {name}: {marks_str}")

                result = "Pass" if marks >= 35 else "Fail"

                if marks >= 80:
                    grade = "A"
                elif marks >= 60:
                    grade = "B"
                else:
                    grade = "C"

                total_marks += marks
                count += 1

                if marks > topper_marks:
                    topper_marks = marks
                    topper_name = name

                outfile.write(f"{name},{age},{marks},{result},{grade}\n")

        if count > 0:
            print("\n--- Students Summary ---")
            print("Class Average:", round(total_marks / count, 2))
            print("Topper:", topper_name, topper_marks)

    except FileNotFoundError:
        print("Students file not found.")
    except ValueError as e:
        print("Error:", e)


process_students_csv()