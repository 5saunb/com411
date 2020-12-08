
class Planet:
  
  def __init__(self):
    self.inhabitants ={"humans":[],"robots":[]}
    self.humans = []
    self.robots = []
  
  def add_human(self,name):
    self.inhabitants["humans"].append(name)
  
  def remove_human(self,name):
    self.humans.remove(name)
  
  def add_robot(self,name):
    self.robots.append(name)

  def remove_robot(self,name):
    self.robots.remove(name)

  def __repr__(self):
    return f"(Robots ={self.inhabitants}, Humans = {self.humans})"
  
  def __str__(self):
    return f"There are {self.humans} humans on the planet and {self.robots} robots!"

planet = Planet()
print(planet.__repr__())
planet.add_human("Darth Vader")
planet.add_human("Bob")
print(planet.__repr__())