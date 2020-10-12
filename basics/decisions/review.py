#Basic User input
print("""
Wake up Neo...""")

input()

print("Do you want to see how far the rabbit hole goes? (yes/no)")
answer = input()
#Answer as Yes
if answer == "yes":
  print("""The choice is yours...
  Take the blue pill and you wake up in your apartment and this is nothing but a dream.
  Take the red pill and I will show you how to free your mind.
  Well...
  Red, or Blue?""")
pill = input()


if (pill == "blue") or (pill == "red"):
  print("*gulp")
elif pill == "blue":
     print("*Neo dies from indecision")
elif pill == "blue":
  print("*Neo wakes up in his bed, a damp sweat on his brow.")
elif pill == "red":
  print ("DOOM")
