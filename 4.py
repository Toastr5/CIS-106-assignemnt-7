
quit = input("would you like to quit(y/n): ")

total_gross_pay = 0
while quit != "y":
  employee_name = input("Enter employee name: ")
  work_code = str(input("Enter employee work code: "))
  
  while work_code.capitalize() not in("L","J","A"): 
    work_code = input("Please enter proper work code: ")
  
  hours_worked = float(input("Enter hours worked: "))
  
  def gross_pay_function(work_code):
    if work_code == "L":
      hourly_rate = 25
      return hourly_rate
    elif work_code == "J":
      hourly_rate = 50
      return hourly_rate
    else:
      hourly_rate = 30 
      return hourly_rate
  
  hourly_rate = gross_pay_function(work_code)
  overtime = hours_worked % 40 * hourly_rate * 1.5 if hours_worked > 40 else 0
  gross_pay = (hours_worked*hourly_rate) + overtime

  print(F"Emplyee: {employee_name}")
  print(F"Gross Pay: {gross_pay}")

  total_gross_pay = total_gross_pay + gross_pay
  quit = input("\nwould you like to quit(y/n): ")

print(F"\nTotal gross pay: {total_gross_pay}")