#Ask the user for input
print("""
Program Started!
Please enter a letter:""")
letter = input()

if (letter == len (1)):
  print("The ASCII code for {} is: {}".format (letter,ord(letter))

else:
  print("That is not a single letter!")
  
print("Program Ended!")