quit = input("would you like to quit(y/n): ")
total_cost = 0
while quit != "y":
  quantity = int(input("Enter quantity of items: "))
  price_per_unit = float(input("Enter price per unit: "))

  def total_price_function(quantity, price_per_unit):
    total_price = quantity * price_per_unit
    if total_price > 100000.00:
      discount_price = total_price - (total_price*.1)
      print(f"\n*Discount added ${total_price*.1}*\n")
    else:
      discount_price = total_price
      print("\n*No discount added*\n")
    return discount_price

  discount_price = total_price_function(quantity, price_per_unit)
  
  print(f"\nQuantity: {quantity}") 
  print(f"Price per unit: ${price_per_unit}")
  print(f"Total price: ${discount_price}")
 
  total_cost = total_cost + discount_price
  quit = input("\nwould you like to quit(y/n): ")

print(f"\nTotal cost: ${total_cost}")
  
  