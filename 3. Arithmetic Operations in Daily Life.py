# Task 1: Grocery Store Math
bread = 1.97
peanut_butter = 3.98
strawberry_preserves = 3.74
sales_tax = .0895 # This is the sales tax where I live but obviously different places have different taxes
groceries_price_before_tax = (bread + peanut_butter + strawberry_preserves)
groceries_price = round(groceries_price_before_tax + groceries_price_before_tax * sales_tax, 2)
print(groceries_price) # Dang, that's expensive

# Task 2: Bank Interest
initial_amount = float(input("Enter initial amount in savings account (example: if its $10,000 write 10000): "))
interest_rate = float(input("Enter yearly interest rate (example: if it's 7% write 0.07): "))
end_year_amount = round((initial_amount + initial_amount * interest_rate), 2)
print("The amount of money you'll have in a year is $" + str(end_year_amount))