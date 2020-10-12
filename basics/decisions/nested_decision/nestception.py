#Intitial User input
print("""
Hi!
I'm Beep, the friendly neighbourhood robot. Like WALL-E but without the movie and merchandising contract.
I'm in a bit of a predicament...
I'm running out of battery and for us robots, that means certain death. As you might imagine, I want to avoid this.
Where should I look for my battery?
""")
room = input()

#First location
if room == "bedroom":
  print("""
  In the bedroom?
  Where in the bedroom should I look?""")
  bedroom = input()
  if bedroom =="under the bed":
    print ("Found some shoes, but no battery!")
  else:
    print ("Found some mess but not my battery")
#Second location
elif room == "lab":
  print("Where in the lab should I look?")
  lab = input()
  if lab == "on the table":
    print("Hurrah! My life is saved! You have found my Battery")
  else:
    print("Dang! Found some tools, but no battery")
#Third location
elif room == "bathroom":
  print ("Water and electricity don't mix! Where in the bathroom should I look?")
  bathroom = input()
  if bathroom == "in the bathtub":
    print("Found a rubber ducky named Geoff but no battery")
  else:
    print("Found a wet surface but no battery")
else:
  print("I don't know where that is! Cripes...this might be the end for me...Better keep looking")

