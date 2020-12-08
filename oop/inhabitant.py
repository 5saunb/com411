class Inhabitant:
  MAX_ENERGY = 100
  MIN_ENERGY = 0
  
  def __init__ (self, name ="Inhabitant", age = 0, energy = MAX_ENERGY):
    pass
    self.name = "Inhabitant"
    self.age = 0
    self.energy = Inhabitant.MAX_ENERGY
  
  def __repr__(self):
    return f"Human(name={self.name},age={self.age},energy={self.energy})"

  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old."
 
  def grow(self):
    self.age =+ 1
  
  def eat(self,food):
    if (self.energy + food) > Inhabitant.MAX_ENERGY:
      self.energy = Inhabitant.MAX_ENERGY
    else:
      self.energy = (self.energy +food)

  def move(self,movement):
    if (self.energy - movement) < Inhabitant.MIN_ENERGY:
      self.energy = Inhabitant.MIN_ENERGY
    else:
      self.energy = (self.energy - movement)