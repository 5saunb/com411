class Robot:
  #Class Attribute
  laws = "Protect,Obey and  Survive"

  #A Class Method
  def the_laws():
    print(Robot.laws)

  #an initialiser (Special Instance Method)
  def __init__(self):

    #An instance attribute
    self.name = "ED209"
    self.age = 0

  #an instance method
  def display(self):
    print(f"I am {self.name}. You have 20 seconds to comply")


class Human:

  #Class Attribute
  MAX_ENERGY = 100

  #Instance attributes
  def __init__(self):

    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def display(self):
    print(f"I am {self.name}! Cower in my shadow!")



