with open(r"C:\Users\Nithin G J\Desktop\Phase1\Day6\Nithin G J\message.txt")as file:
    print("reading line by line :")
    for line in file:
        clean_lines=line.strip()
        print("clean line:",repr(clean_lines))