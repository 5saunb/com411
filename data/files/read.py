def search(filename):
  print("Searching...")
  with open(filename) as file:
   for line in file:
     print("Looked in {}".format(line)) 
  print("...Done!")

def run():

  search("data/files/locations.txt")  

run()