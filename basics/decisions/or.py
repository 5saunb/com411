#First user input
print("""
Hi!
I'm starting to feel adventurous, like I should go on an adventure. There's just the one problem...
I don't know what type of adventure I should have!
What do you suggest?""")
adventure = input()
#first or condition
if (adventure == "short") or (adventure == "scary"):
  print("""
  Ok!
  I'll enter the dark forest!
  Hopefully no monsters have the taste for robots""")
#second or condition
elif (adventure == "long") or (adventure == "safe"):
  print("""
  Ok then!
  Boring, but I'll live to see another day.
  Taking the safe route""")
#otherwise
else:
  print("""
  The {} route?!!
  Are you mad!!
  I'm not going there!""".format (adventure))
  