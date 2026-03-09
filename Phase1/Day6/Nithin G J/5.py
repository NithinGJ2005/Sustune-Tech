# step 10 write a transformed csv with result column
with open("students.csv","r")as infile,open("students_result.csv","w")as outfile:
    header=infile.readline().strip()
    outfile.write(header +",Result\n")
    for line in infile:
        line=line=line.strip()
        if not line:
            continue
        name,age,marks=line.split(",")
        marks=int(marks)
        if marks>=60:
            result="pass"
        else:
            result="fail"
        new_line=f"{name},{age},{marks},{result}\n"
        outfile.write(new_line)
print("students_result.csv created")
        
 #step11 safe processing funtions with error handling
def process_students_csv(input_path,output_path):
    try:
        with open(input_path,"r") as infile,open(output_path,"w")as outfile:
            header=infile.readline().strip()
            outfile.write(header+"Result\n")
            for line in infile:
                line=line.strip()
                if not line:
                    continue
                parts=line.split(",")
                if len(parts)!=3:
                    print("skipping invalid line:",line)
                    continue
                name,age,marks=parts
                try:
                    marks=int(marks)
                except ValueError:
                    print("invalid marks for",name,"-->",marks)
                    continue
                result="pass" if marks>=60 else "fail"
                new_line=f"{name},{age},{marks},{result}\n"
                outfile.write(new_line)
            print("processing completed successfully.")
    except FileNotFoundError:
        print("error:file not found")
    except Exception as e:
        print("unexpected error",e)
process_students_csv("students.csv","students_result.csv")