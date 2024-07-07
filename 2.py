print("Type stop to end program")
name = input("Give players last name: ")
at_bat = int(input("Give number of times at bats: "))
hits = int(input("Give number of hits: "))
total_players = 0

while name != "stop":
  
  def batting_average_function(name, at_bat, hits):
    batting_average = hits / at_bat
    print(F"Player: {name}")
    print(F"Batting Average: {batting_average}")
    
  total_players = total_players + 1
  
  batting_average_function(name, at_bat, hits)
  
  print("\nType stop to end program")
  name = input("Give players last name: ")
  at_bat = int(input("Give number of times at bats: "))
  hits = int(input("Give number of hits: "))

print(f"\nTotal players: {total_players}")