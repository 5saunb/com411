#Define the first function -display in box
def dis_box(word):
  num_dashes = (len(word)+2)
  print("-" *(num_dashes))
  print("|{}|".format(word)) 
  print("-" *(num_dashes))
#Define the second function -Diplay Lower case
def dis_lower(word):
  print(word.lower())
#define the thrid function - display in upper cas
def dis_upper(word):
  print(word.upper())
#define the fourth function - display mirrored
def dis_mirror(word):
  print(word, "|" ,word[::-1])
#define the fifthe function - display the word
def dis_repeat(word):
  print(word * num_rep)
#Define the Run function
def run():
  print("Please type a word")
  word = input()
  print("""
  1) Display in a Box 
  2) Display Lower-case 
  3) Display Upper-case
  4) Display Mirrored 
  5) Repeat 
  Please enter a number from 1-5 to pick the function...""")
  num = int(input())
  if (num == 1):
    dis_box(word)
  elif (num == 2):
    dis_lower(word)
  elif (num == 3):
    dis_upper(word)
  elif (num == 4):
    dis_mirror(word)
  elif (num == 5):
    print("How many repetitions?")
    num_rep = int(input())
    dis_repeat(word)


#RUN THE PROGRAM
run()