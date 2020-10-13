#Define Function 
def cross_bridge(steps):
  num = 0
  while (steps > num):
    print("Crossed Step.")
    num = num +1
  if steps > 5:
    print("The bridge is collapsing!")
  else:
    print("We must keep going!")

cross_bridge(3)
cross_bridge(6)


print("The bridge is collapsing!")


git 