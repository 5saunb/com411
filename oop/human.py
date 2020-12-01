class Robot:
  #Class Attribute
  laws = "Protect,Obey and  Survive"
  MAX_ENERGY = 100
  MIN_ENERGY = 0
  #A Class Method
  def the_laws():
    print(Robot.laws)

  
  def __repr__(self):
    return f"Robot(name={self.name},age={self.age})"

  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old."

  #an initialiser (Special Instance Method)
  def __init__(self):

    #An instance attribute
    self.name = "ED209"
    self.age = 0

  #an instance method
  def display(self):
    print(f"I am {self.name}. You have 20 seconds to comply")

  def grow(self):
    self.age =+ 1
  
  def move(self,movement):
    if (self.energy - movement) < Robot.MIN_ENERGY:
      self.energy = Robot.MIN_ENERGY
    else:
      self.energy = (self.energy - movement)
  def eat(self,food):
    if (self.energy + food) > Robot.MAX_ENERGY:
      self.energy = Robot.MAX_ENERGY
    else:
      self.energy = (self.energy +food)

class Human:

  #Class Attribute
  MAX_ENERGY = 100
  MIN_ENERGY = 0

  #Instance attributes
  def __init__(self):

    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def display(self):
    print(f"I am {self.name}! Cower in my shadow!")
  
  def __repr__(self):
    return f"Human(name={self.name},age={self.age},energy={self.energy})"

  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old."

  def grow(self):
    self.age =+ 1
  
  def eat(self,food):
    if (self.energy + food) > Human.MAX_ENERGY:
      self.energy = Human.MAX_ENERGY
    else:
      self.energy = (self.energy +food)

  def move(self,movement):
    if (self.energy - movement) < Human.MIN_ENERGY:
      self.energy = Human.MIN_ENERGY
    else:
      self.energy = (self.energy - movement)

human = Human()
human.grow()
human.display()
print(human.__repr__())
print(human.__str__())
human.eat(2)
print(human.__repr__())
human.move(120)
print(human.__repr__())