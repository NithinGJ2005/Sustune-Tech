#Filtering example: even numbers
number=[3,10,7,2,15,8,21,14]
even_numbers=[]
for n in number:
    if n%2==0:
        even_numbers.append(n)
        
print("original list:",number)
print("Even numbers:",even_numbers)


number=[3,10,7,2,15,8,21,14]
great_numbers=[]
for n in number:
    if n>10:
        great_numbers.append(n)
        
print("original list:",number)
print("greater than 10 numbers:",great_numbers)



#Filtering example2: students above 75
students=[("navami",85),("akash",72),("devika",91),("shreya",65),("nithin",78)]
top_students=[]
for name,marks in students:
    if marks>75:
        top_students.append((name,marks))
print("all students:",students)
print("Top students:",top_students)



students=[("navami",85),("akash",72),("devika",91),("shreya",65),("nithin",78)]
pass_students=[]
for name,marks in students:
    if marks>=60:
        pass_students.append((name,marks))
print("\nall students:",students)
print("\npass students:",pass_students)





#sorting example 1: numbers
numbers=[3,10,7,2,15,8,21,14]
asceding=sorted(numbers)
descending=sorted(number,reverse=True)
print("\nNumbers",numbers)
print("\nAscending:",asceding)
print("\ndescending:",descending)

#for smallest 3 numbers
small_3=asceding[:3]
print(small_3)

#sorting example 2: students by marks
students=[("navami",85),("akash",72),("devika",91),("shreya",65),("nithin",78)]
students_sorted_by_marks=sorted(students,key=lambda s:s[1],reverse=True)
print("Student sorted by marks(high to low)")
for name,marks in students_sorted_by_marks:
    print(name,"-",marks)

#sorting example 2: students by marks
students=[("navami",85),("akash",72),("devika",91),("shreya",65),("nithin",78)]
students_sorted_by_names=sorted(students,key=lambda s:s[0])
print("Student sorted by marks(high to low)")
for name,marks in students_sorted_by_names:
    print(name,"-",marks)


#aggregation example1:numbers
numbers=[3,10,7,2,15,8,21,14]
total=sum(numbers)
count=len(numbers)
average=total/count
minimum=min(numbers)
maximum=max(numbers)
print("total: ",total,"\ncount ",count,"\naverage",average, "\nmim",minimum,"\nmax",maximum)

#aggregation example2:student marks
students=[("navami",85),("akash",72),("devika",91),("shreya",65),("nithin",78)]
marks_list=[marks for name,marks in students]
taotal_marks=sum(marks_list)
average_marks=taotal_marks/len(marks_list)
higest_marks=max(marks_list)
lowest_marks=min(marks_list)
print("taotal marks:",taotal_marks)
print("average",average_marks)
print("minimum marks",lowest_marks)
print("highest marks",higest_marks)




students=[("navami",85),("akash",72),("devika",91),("shreya",65),("nithin",78)]
passed_students=[]
failed_students=[]
for name,marks in students:
    if marks>=60:
        passed_students.append((name,marks))
    else:
        failed_students.append((name,marks))
print("\npassed students are",passed_students)
print("\nfailed students are",failed_students)


#normal way
numbers=[1,2,3,4,5]
squares=[]
for n in numbers:
    squares.append(n*n)

#list comprehension method
squares2=[n*n for n in numbers]
print("squares:",squares)
print("squraes2:",squares2)

#filtering with comprehension
numbers=[3,10,7,2,15,8,21,14]
even_numbers=[n for n in numbers if n%2==0] 
print("even NOs(comprehension)",even_numbers)


students=[("navami",85),("akash",72),("devika",91),("shreya",65),("nithin",78)]
names=[name for name,marks in students if marks>=75]
print("name",names)




students = [
    ("Navami", 85),
    ("Akash", 72),
    ("Devika", 91),
    ("Shreya", 55),
    ("Nithin", 78),
    ("Komal", 40),
]
distinction_students = [name for name, marks in students if marks >= 80]
print("\n\ndistinction student:", distinction_students)
passed_students = [name for name, marks in students if marks >= 60]
print("passed student:", passed_students)
failed_students = [name for name, marks in students if marks < 60]
print("failed student:", failed_students)
print("distinction:", len(distinction_students))
print("passed:", len(passed_students))
print("failed:", len(failed_students))



products = [
    ("Pen", 20, 10),
    ("Notebook", 50, 5),
    ("Pencil", 5, 30),
    ("Marker", 25, 8),
    ("Eraser", 10, 15),
]
price_from_high_to_low=sorted(products,key=lambda s:s[1],reverse=True)
quantity_from_high_to_low=sorted(products,key=lambda s:s[2],reverse=True)
calculated_value=[]
print("\n\noriginal list:",products)
print("\n\nprices for high to low:",price_from_high_to_low)
print("\n\nquantity from high to low:",quantity_from_high_to_low)
for product,price,quantity in products:
    value=price*quantity
    calculated_value.append((product,price,quantity,value))
print("\n\ncalculated values:",calculated_value)
highest_value_product_to_lowest=sorted(calculated_value,key=lambda s:s[3],reverse=True )
print("\n\nhighest value product to lowest:",highest_value_product_to_lowest)





sales = [
    ("Pen", 10, 20),
    ("Notebook", 3, 50),
    ("Pencil", 20, 5),
    ("Pen", 5, 20),
    ("Eraser", 10, 10),
    ("Notebook", 2, 50),
]

product_totals = {}
grand_total = 0
for product, quantity, price in sales:
    amount = quantity * price
    grand_total += amount
    if product in product_totals:
        product_totals[product] += amount
    else:
        product_totals[product] = amount
print("Total sales per product:")
for product, total in product_totals.items():
    print(product, ":", total)
print("\nGrand total sales:", grand_total)
top_product, highest_sale = max(product_totals.items(), key=lambda x: x[1])
print("Top product with highest sale:", top_product, "-", product_totals[top_product])
