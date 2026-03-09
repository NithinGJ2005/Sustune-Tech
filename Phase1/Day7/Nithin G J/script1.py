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



#another way of doing the 1st code #filtering the students..

students=[("Navami", 85),("Akash", 72),("Devika", 91),("Shreya", 55),("Nithin", 78),("Komal", 40)]
passed_students=[]
distinction_students=[]
failed_students=[]
for name , marks in students:
    if marks>=60:
        passed_students.append((name,marks))
    if marks>=80:
        distinction_students.append((name,marks))
    if marks<60:
        failed_students.append((name,marks))
print("Passed Students are: ",passed_students)
print("Distinction Students are: ",distinction_students)
print("Failed students are: ",failed_students)

count_passed=len(passed_students)
count_distinction=len(distinction_students)
count_failed=len(failed_students)

print("Passed; ",count_passed)
print("Distinction: ",count_distinction)
print("Failed: ",count_failed)