try:
    product_totals = 0
    grand_total = 0

    with open("sales.csv", "r") as infile, open("sales_report.csv", "w") as outfile:
        header = infile.readline().strip()
        outfile.write(header + ",TotalAmount\n")

        for line in infile:
            line = line.strip()
            if not line:
                continue

            
            date, product, qty, price = line.split(",")
            qty = int(qty)
            price = float(price)

            total_amount = qty * price
            grand_total += total_amount

            outfile.write(f"{date},{product},{qty},{price},{total_amount}\n")
            print("result:",product,total_amount)

            



    print("\nGrand Total Sales:", grand_total)
    print("sales_report.csv created successfully")

except FileNotFoundError:
    print("Error: sales.csv file not found")