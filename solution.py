Item_price:int = 12
tax_rate:float = 0.15
quantity_item:int = 5

subTotal = Item_price * quantity_item
tax_amount = subTotal * tax_rate
total_price = subTotal + tax_amount
print("Item price:","SAR", Item_price, "\nQuantity:", quantity_item, "\nTax rate:", tax_rate * 100, "%")
print("\n======================\n")
print("Subtotal:","SAR", subTotal, "\nTax amount:","SAR", tax_amount, "\nTotal Price:","SAR", total_price)
