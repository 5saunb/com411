#User input
print("What type of cover does the book have?")
cover = input()

if cover == "soft":
  print("Is the book perfect-bound (yes/no)")
  bind = input()
  if bind == "yes":
    print("Soft cover, perfect bound books are exceedingly popular!")
  else:
    print("Soft covers with coils or stitches are great for short books")

else:
  print("Books with hard covers can be more expensive")

