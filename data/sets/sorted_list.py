def observed():
  for count in range (5):
    print("Enter an observation")
    item = input()
    observations = []
    observations.append(item)
  return observations

def remove_observations(observations):
  is_running = True
  
  while(is_running == True):
    print("Do you wish to remove an observation? (yes/no)")
    answer =input()

    if (answer == "yes"):
      print("Which obeservation would you like to remove?")
      to_remove = input()
      observations.remove(to_remove)


    else:
      is_running = False


def run():
  observations = observed()
  remove_observations(observations)

  observation_set = set()
  
  for observation in observations:
    occurences = observations.count(observation)
    observations_set.add ((observation,occurences))
  
  print ("Observations:")
  for key, value in sorted(observation_set):
    print(f"{key} observed {value} times!")

run()