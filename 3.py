quit = input("would you like to quit(y/n): ")

total_trips = 0
while quit != "y":
  city = input("Enter your destination: ")
  miles = float(input("Enter the miles to your destination: "))
  gallons = float(input("Enter the gallons of gas used: "))

  def mpg_function(miles, gallons):
    mpg = miles/gallons
    return mpg
  mpg = mpg_function(miles, gallons)
  print(f"Your mpg is {mpg}")
  total_trips = total_trips + 1
  quit = input("would you like to quit(y/n): ")
  
print(F"Total trips: {total_trips}")
