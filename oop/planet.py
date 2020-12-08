<<<<<<< HEAD
from human import Human
from human import Robot

class Planet:
  
  num_humans = 0
  num_robots = 0

  def __init__(self):
    self.inhabitants = []

  
  def add_inhabitant(self,name,):
    self.inhabitants.append(name)
    for inhabitant in planet.inhabitants:
      if isinstance(inhabitant,Robot):
       Planet.num_robots += 1
  
      elif isinstance (inhabitant,Human):
        Planet.num_humans+= 1
  def remove_inhabitant(self,name):
    self.inhabitants.remove(name)

  def __repr__(self):
    return f"(Robots={Planet.num_robots}, Humans ={Planet.num_humans} , Inhabitants ={self.inhabitants})"
  
  def __str__(self):
    return f"There are {Planet.num_humans} humans on the planet and {Planet.num_robots} robots!"

 
    
    


planet = Planet()
print(planet.__repr__())
planet.add_inhabitant("Darth Vader", Human)
planet.add_inhabitant("Bob")
print(planet.__repr__())
print(planet.inhabitants)
=======

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
>>>>>>> 7d0657b774cb0de32af45528bfc49a1268deb940
