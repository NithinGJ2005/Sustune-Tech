#create a simple text file
with open("message.txt","w") as file:
    file.write("Hello VRV")
    file.write("\nwelcome to day6-File IO \n")
# read the text file
file=open("message.txt","r")
content=file.read()
print("Readings with mnaual open/close:")
print(content)
file.close()

#safer way using with
with open("message.txt","r") as file:
    content=file.read()
    print("Readings with WITH block:")
    print(content)
    
with open("notes.txt","w")as vrv:
    vrv.write("hello bro whats up")
    vrv.write("\ni am learning file")
    
with open("notes.txt","r") as file:
    content=file.read()
    print("Readings with WITH block:")
    print(content)
    
#reading line by line
with open("message.txt","r") as file:
    print("Reading Line by Line")
    for line in file:
        print("raw line:",repr(line))


with open("message.txt","r")as file:
    print("reading line by line :")
    for line in file:
        clean_lines=line.strip()
        print("clean line:",repr(clean_lines))
        
        
with open("students_names.txt","w")as vrv:
    vrv.write("vinay\n")
    vrv.write("vvrvrv\n")
    vrv.write("hello vvv\n")
with open("students_names.txt")as vrv:
    for line in vrv:
        clean_lines=line.strip()
        print("students",repr(clean_lines))