name = input("Enter customer name: ")
item = input("Enter item name: ")
item_quantity = int(input("Quantity of item: "))

price = 78
tax_rate = 0.05

subtotal = price * item_quantity
total = subtotal + (tax_rate * subtotal)

print("\n--- BILL ---")
print("Customer Name:", name)
print("Item:", item)
print("Quantity:", item_quantity)
print("Price per item: ₹", price)
print("Subtotal: ₹", subtotal)
print("Total after tax (5%): ₹", round(total, 2))