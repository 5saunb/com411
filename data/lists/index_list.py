#define function movements
def movements():
  path = [ "Move Forward", 10, "Move Backward", 5, "Move Left", 3,"Move Right", 1]
  return path

def run():
  print("Moving...")

  movements()

  local = movements()

  print("{} for {} steps".format(local[0], local[1]))
  print("{} for {} steps".format(local[2], local[3]))
  print("{} for {} steps".format(local[4], local[5]))
  print("{} for {} steps".format(local[6], local[7]))

run()