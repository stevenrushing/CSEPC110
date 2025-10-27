# The extra creative part is to verify that the payment amount is enough to pay the bill.

# What is the price of a child's meal? 4.50
# What is the price of an adult's meal? 9.00
# How many children are there? 4
# How many adults are there? 2

# Subtotal: $36.00

# What is the sales tax rate? 6
# Sales Tax: $2.16
# Total: $38.16

# What is the payment amount? 40
# Change: $1.84

child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))
print()
subtotal = child_meal * num_children + adult_meal * num_adults
print(f"Subtotal: {subtotal:.2f}")
print()
tax_rate = float(input("What is the sales tax rate? "))
sales_tax = subtotal * tax_rate / 100
print(f"Sales Tax: ${sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")
print()

payment_amount = float(input("What is the payment amount? "))
while payment_amount < total: 
    payment_amount = float(input(f"Please enter an amount more than ${total:.2f}: "))


change = payment_amount - total
print(f"Change: ${change:.2f}")