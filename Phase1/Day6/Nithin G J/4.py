with open("students.csv","w")as file:
    file.write("Name,Age,Marks\n")
    file.write("vrv,20,85\n")
    file.write("vvv,22,60\n")
    file.write("vinay,21,99\n")
    
    
    
#step7 read the csv and split
with open("students.csv","r") as file:
    print("Reading students.csv:")
    for line in file:
        line=line.strip()
        parts=line.split(",")
        print(parts)
        
        
#step8 skip header and read data rows
with open("students.csv","r")as file:
    header=file.readline().strip()
    print("Header",header)
    print("data rows:")
    for line in file:
        line=line.strip()
        if not line:
            continue
        parts=line.split(",")
        name,age,marks=parts
        print("student:",name)
        
        
#step9 calculate average marks from CSV
total_marks=0
count=0
with open("students.csv","r")as file:
    header=file.readline()
    for line in file:
        line=line.strip()
        if not line:
            continue
        name,age,marks=line.split(",")
        marks=int(marks)
        total_marks+=marks
        count+=1
        if marks>=75:
            print("Topper",name,marks)
average=total_marks/count
print("average marks",average)    