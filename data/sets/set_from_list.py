def observed():
  observations = []

  for count in range (7):
    print("Please enter an observation")
    observations.append(input(""))
  return observations
  

def run():
  print("Counting observations...")
  observations = observed()
  observed_set = set()

  for observation in observations:
    observed_set.add((observation,observations.count(observation)))
  
  for key, value in observed_set:
    print ("{} observed {} times.".format(key, value))
  

run()

