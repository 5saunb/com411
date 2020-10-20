#Define the first function
def directions():
  directions = ["Move Forward", "Move Backward","Turn Left","Turn Right"]
  return directions

#Define the second function
def menu():
  print("Please select a direction")
  directions()
  
  menu_opt = directions()
  
  for index in range(len(menu_opt)):
    print("{}: {}".format(index, menu_opt[index]))

  menu_select = int(input())
  return menu_select

#Define the run function
def run():  
  route = []
  print("Working out escape route...")
  
  loop = 0
  while loop < 5:
    
    local = menu()
    route.append(local)
  
    loop = loop +1

  print(route)

 

run()