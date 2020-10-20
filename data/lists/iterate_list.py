def directions():
  directions = ["Move Forward", "Move Backward","Turn Left","Turn Right"]
  return directions

def menu():
  print("Please select a direction")
  directions()
  
  menu_opt = directions()
  
  for index in range(len(menu_opt)):
    print("{}: {}".format(index, menu_opt[index]))

def run():
  menu()

run()