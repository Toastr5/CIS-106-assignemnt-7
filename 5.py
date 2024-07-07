quit = input("would you like to quit(y/n): ")
total_tuition = 0

while quit != "y":
  student_name = input("Enter students name: ")
  district_code = input("Enter district code: ")

  while district_code.capitalize() not in ("I","O"): 
    work_code = input("Please enter proper district code: ")

  credit_hours = float(input("Enter credit hours: "))

  def district_code_function(district_code):
    if district_code == "I":
      credit_rate = 250
      return credit_rate
    else:
      credit_rate = 550 
      return credit_rate

  hourly_rate = district_code_function(district_code)
  tuition = hourly_rate * credit_hours

  print(F"Student: {student_name}")
  print(F"Tuition: {tuition}")

  total_tuition = total_tuition + tuition
  quit = input("\nwould you like to quit(y/n): ")

print(F"\nTotal tuition: {total_tuition}")