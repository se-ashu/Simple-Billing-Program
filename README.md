
# Simple Billing Program 🧾

This is a basic Python program that generates a simple bill for a customer purchase.  
It takes user input for customer name, item name, and item quantity, then calculates the subtotal and total after applying a 5% tax.

---

## Features
- Accepts customer name, item name, and quantity as input.
- Uses a fixed price (`₹78`) per item (can be modified).
- Applies a **5% tax rate** to the subtotal.
- Displays a formatted bill with all details.

---

## Requirements
- Python 3.x

---

## How to Run
1. Save the code in a file named `billing.py`.
2. Open a terminal or command prompt.
3. Run the program:
   ```bash
   python billing.py
   ```
4. Enter the required details when prompted.

---

## Example Run
```
Enter customer name: Ramesh
Enter item name: Notebook
Quantity of item: 3

--- BILL ---
Customer Name: Ramesh
Item: Notebook
Quantity: 3
Price per item: ₹ 78
Subtotal: ₹ 234
Total after tax (5%): ₹ 245.7
```

---

## Possible Improvements
- Allow dynamic price input instead of hardcoding.
- Add support for multiple items (shopping cart).
- Save bills to a file for record-keeping.
- Improve formatting with f-strings for cleaner output.

---

## License
This project is free to use and modify for learning purposes.
```

---
