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
  print ("{} observed {} times.".format(observed_set, observed_set.count()))
  

run()

