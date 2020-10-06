#User prompt for direction of painbrush
print("Beep, the robot, is going to try and paint a picture. Which direction should he move his brush in? (up, down, left or right?")
direction = input()

if (direction == "up"):
  print ("I'm painting upwards!")

elif direction == "down" :
  print ("I'm going to paint down!")

elif direction == "right" :
  print("Right it is then!")

elif direction == "left":
  print("left we go!")

else:
  print("I don't understand...was that a direction?")
  
print("Analysis complete!")

